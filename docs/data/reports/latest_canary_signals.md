# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T14:52:29.770478+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1133` n `13`; crypto_alt avg `0.3847` n `237`; crypto_major avg `0.2741` n `8`; equity avg `0.5063` n `152`; fx avg `0.0062` n `6`; index avg `0.1274` n `26`; metal avg `0.103` n `20`; unknown avg `0.7676` n `1233`
- 1h: commodity avg `-0.0873` n `13`; crypto_alt avg `0.1299` n `237`; crypto_major avg `0.0386` n `8`; equity avg `0.6858` n `152`; fx avg `0.0378` n `6`; index avg `0.1422` n `26`; metal avg `-0.0245` n `20`; unknown avg `0.3832` n `1175`
- 4h: commodity avg `-0.0673` n `13`; crypto_alt avg `0.2177` n `237`; crypto_major avg `0.3131` n `8`; equity avg `0.505` n `152`; fx avg `0.0285` n `6`; index avg `0.1402` n `26`; metal avg `-0.0008` n `20`; unknown avg `0.0314` n `1161`
- 24h: commodity avg `0.3236` n `13`; crypto_alt avg `0.7919` n `237`; crypto_major avg `0.3865` n `8`; equity avg `0.258` n `152`; fx avg `-0.0159` n `6`; index avg `0.0782` n `26`; metal avg `-0.3651` n `20`; unknown avg `-0.4031` n `984`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1944`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
