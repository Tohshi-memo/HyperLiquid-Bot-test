# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T20:52:40.256136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0559` n `13`; crypto_alt avg `-0.0194` n `237`; crypto_major avg `-0.0072` n `8`; equity avg `0.3208` n `151`; fx avg `-0.0025` n `6`; index avg `0.0535` n `26`; metal avg `0.0148` n `20`; unknown avg `1.2091` n `1199`
- 1h: commodity avg `-0.0194` n `13`; crypto_alt avg `0.3008` n `237`; crypto_major avg `0.2822` n `8`; equity avg `0.6529` n `151`; fx avg `-0.0083` n `6`; index avg `0.1096` n `26`; metal avg `0.0307` n `20`; unknown avg `44.2867` n `1149`
- 4h: commodity avg `0.1538` n `13`; crypto_alt avg `0.0774` n `237`; crypto_major avg `0.2239` n `8`; equity avg `0.482` n `151`; fx avg `-0.0075` n `6`; index avg `0.0927` n `26`; metal avg `0.014` n `20`; unknown avg `15.416` n `1133`
- 24h: commodity avg `-0.0581` n `13`; crypto_alt avg `3.1101` n `237`; crypto_major avg `2.0126` n `8`; equity avg `0.7941` n `151`; fx avg `0.0135` n `6`; index avg `0.1064` n `26`; metal avg `0.0609` n `20`; unknown avg `5.0825` n `1034`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
