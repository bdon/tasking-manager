import React from 'react';
import { Link } from '@gatsbyjs/reach-router';
import { FormattedMessage } from 'react-intl';

import messages from './messages';

export default function ClearFilters({ url, className = '' }: Object) {
  return (
    <Link to={url} className={`red link ph3 pv2 f6 ${className}`}>
      <FormattedMessage {...messages.clearFilters} />
    </Link>
  );
}
