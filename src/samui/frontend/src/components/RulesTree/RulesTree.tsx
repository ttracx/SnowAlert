import {
  // Icon,
  Tree,
  Input,
} from 'antd';
import * as React from 'react';
import {connect} from 'react-redux';
import {bindActionCreators, Dispatch} from 'redux';

import {loadSnowAlertRules, changeRule} from '../../actions/rules';
import {getRules} from '../../reducers/rules';

import {State, SnowAlertRule, SnowAlertRulesState} from '../../reducers/types';

import './RulesTree.css';

const TreeNode = Tree.TreeNode;
const Search = Input.Search;

interface OwnProps {
  target: SnowAlertRule['target'];
}

interface DispatchProps {
  loadSnowAlertRules: typeof loadSnowAlertRules;
  changeRule: typeof changeRule;
}

interface StateProps {
  rules: SnowAlertRulesState;
}

type RulesTreeProps = OwnProps & DispatchProps & StateProps;

class RulesTree extends React.PureComponent<RulesTreeProps> {
  componentDidMount() {
    this.props.loadSnowAlertRules();
    this.props.changeRule('');
  }

  setFilter = (value: string) => {
    this.props.rules.filter = value;
    this.generateTree(this.props.rules.rules, this.props.target);
  };

  generateTree = (rules: SnowAlertRulesState['rules'], target: SnowAlertRule['target']) => {
    const queries: Array<SnowAlertRule> = [];
    const suppressions: Array<SnowAlertRule> = [];
    var filter = this.props.rules.filter;

    for (let rule of rules)
      if (rule.target === target) {
        if (rule.type === 'QUERY' && (filter !== null && rule.title.includes(filter))) {
          queries.push(rule);
        }
        if (rule.type === 'SUPPRESSION' && (filter !== null && rule.title.includes(filter))) {
          suppressions.push(rule);
        }
      }

    return [
      <Search placeholder="Query Name" onSearch={value => this.setFilter(value)} style={{width: 200}} />,
      <TreeNode key="queries" title="Queries" selectable={false}>
        {this.props.rules.isFetching ? (
          <TreeNode title="Loading..." />
        ) : (
          queries.map(r => (
            <TreeNode selectable key={`${r.title}_${target}_QUERY`} title={(r.isSaving ? '(saving) ' : '') + r.title} />
          ))
        )}
      </TreeNode>,
      <TreeNode key="suppressions" title="Suppressions" selectable={false}>
        {this.props.rules.isFetching ? (
          <TreeNode title="Loading..." />
        ) : (
          suppressions.map(r => (
            <TreeNode
              selectable
              key={`${r.title}_${target}_SUPPRESSION`}
              title={(r.isSaving ? '(saving) ' : '') + r.title}
            />
          ))
        )}
      </TreeNode>,
    ];
  };

  render() {
    var rules = this.props.rules.rules;
    return (
      <Tree showLine defaultExpandAll onSelect={x => this.props.changeRule(x[0] || '')}>
        {this.generateTree(rules, this.props.target)}
      </Tree>
    );
  }
}

const mapStateToProps = (state: State) => {
  return {
    rules: getRules(state),
  };
};

const mapDispatchToProps = (dispatch: Dispatch) => {
  return bindActionCreators(
    {
      loadSnowAlertRules: loadSnowAlertRules,
      changeRule,
    },
    dispatch,
  );
};

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(RulesTree);
