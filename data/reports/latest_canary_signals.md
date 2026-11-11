# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T05:52:27.718963+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0501` n `13`; crypto_alt avg `0.0619` n `239`; crypto_major avg `0.1319` n `8`; equity avg `0.2539` n `161`; fx avg `-0.0002` n `6`; index avg `0.0159` n `27`; metal avg `0.0059` n `20`; unknown avg `39.679` n `1259`
- 1h: commodity avg `0.0057` n `13`; crypto_alt avg `-0.3267` n `239`; crypto_major avg `0.0797` n `8`; equity avg `0.4131` n `161`; fx avg `-0.0383` n `6`; index avg `0.0377` n `27`; metal avg `0.1599` n `20`; unknown avg `66.9209` n `1251`
- 4h: commodity avg `0.0483` n `13`; crypto_alt avg `-0.1109` n `239`; crypto_major avg `0.1121` n `8`; equity avg `1.0811` n `161`; fx avg `-0.0629` n `6`; index avg `0.1421` n `27`; metal avg `0.2368` n `20`; unknown avg `8.5581` n `1241`
- 24h: commodity avg `0.1802` n `13`; crypto_alt avg `-0.9521` n `239`; crypto_major avg `-2.5301` n `8`; equity avg `1.4378` n `161`; fx avg `-0.1893` n `6`; index avg `0.1832` n `27`; metal avg `-0.1527` n `20`; unknown avg `23.696` n `1170`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.292`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2658`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
