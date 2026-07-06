# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T06:37:29.153905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0671` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0233` n `12`; crypto_alt avg `0.0302` n `229`; crypto_major avg `0.0046` n `8`; equity avg `0.1117` n `88`; fx avg `-0.0146` n `6`; index avg `0.0275` n `25`; metal avg `0.0353` n `20`; unknown avg `-0.0417` n `763`
- 1h: commodity avg `0.1245` n `12`; crypto_alt avg `-0.0699` n `229`; crypto_major avg `-0.1186` n `8`; equity avg `0.1078` n `88`; fx avg `0.0249` n `6`; index avg `0.0717` n `25`; metal avg `-0.0152` n `20`; unknown avg `0.0072` n `731`
- 4h: commodity avg `0.1533` n `12`; crypto_alt avg `-1.0613` n `229`; crypto_major avg `-0.9442` n `8`; equity avg `0.4518` n `88`; fx avg `-0.0038` n `6`; index avg `0.1229` n `25`; metal avg `-0.1011` n `20`; unknown avg `-0.107` n `731`
- 24h: commodity avg `0.0011` n `12`; crypto_alt avg `-0.049` n `229`; crypto_major avg `0.8486` n `8`; equity avg `-0.6326` n `88`; fx avg `0.0705` n `6`; index avg `-0.0417` n `25`; metal avg `-0.2398` n `20`; unknown avg `1.0177` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
