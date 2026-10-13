# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T02:22:28.051249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0243` n `13`; crypto_alt avg `0.4385` n `235`; crypto_major avg `0.3243` n `8`; equity avg `0.0974` n `151`; fx avg `0.0157` n `6`; index avg `0.0096` n `26`; metal avg `0.0079` n `20`; unknown avg `0.5869` n `1135`
- 1h: commodity avg `-0.0615` n `13`; crypto_alt avg `0.808` n `235`; crypto_major avg `0.8851` n `8`; equity avg `-0.0743` n `151`; fx avg `0.0257` n `6`; index avg `-0.0454` n `26`; metal avg `0.0207` n `20`; unknown avg `0.8947` n `1133`
- 4h: commodity avg `-0.1422` n `13`; crypto_alt avg `-0.8907` n `235`; crypto_major avg `-0.3179` n `8`; equity avg `-1.3084` n `151`; fx avg `0.0603` n `6`; index avg `-0.2902` n `26`; metal avg `-0.0988` n `20`; unknown avg `3.6842` n `1127`
- 24h: commodity avg `0.7025` n `13`; crypto_alt avg `-5.0803` n `235`; crypto_major avg `-3.1264` n `8`; equity avg `-4.7157` n `151`; fx avg `-0.0425` n `6`; index avg `-0.6151` n `26`; metal avg `-0.373` n `20`; unknown avg `0.4697` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.212`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.195`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1241`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1097`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1069`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.103`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.093`, n `666`, weak_sample_signal
