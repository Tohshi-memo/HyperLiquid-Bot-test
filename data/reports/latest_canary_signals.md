# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T19:07:26.849706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0358` n `13`; crypto_alt avg `0.4422` n `239`; crypto_major avg `0.3652` n `8`; equity avg `0.2665` n `162`; fx avg `0.0069` n `6`; index avg `0.0243` n `27`; metal avg `-0.0228` n `20`; unknown avg `2.4973` n `1259`
- 1h: commodity avg `0.0521` n `13`; crypto_alt avg `0.1836` n `239`; crypto_major avg `0.0847` n `8`; equity avg `0.2088` n `162`; fx avg `0.026` n `6`; index avg `0.0163` n `27`; metal avg `0.0173` n `20`; unknown avg `40.3958` n `1259`
- 4h: commodity avg `0.051` n `13`; crypto_alt avg `0.2476` n `239`; crypto_major avg `0.3003` n `8`; equity avg `0.4948` n `162`; fx avg `0.0356` n `6`; index avg `0.0459` n `27`; metal avg `0.1005` n `20`; unknown avg `2.7299` n `1250`
- 24h: commodity avg `0.1034` n `13`; crypto_alt avg `-0.8252` n `239`; crypto_major avg `-0.459` n `8`; equity avg `0.3864` n `162`; fx avg `0.0159` n `6`; index avg `0.0537` n `27`; metal avg `-0.0744` n `20`; unknown avg `1.7909` n `1134`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
