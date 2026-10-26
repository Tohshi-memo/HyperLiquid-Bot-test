# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T22:52:29.995211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0084` n `13`; crypto_alt avg `0.0904` n `237`; crypto_major avg `0.1031` n `8`; equity avg `-0.0429` n `154`; fx avg `-0.018` n `6`; index avg `-0.005` n `27`; metal avg `0.0022` n `20`; unknown avg `-0.1703` n `1238`
- 1h: commodity avg `-0.0184` n `13`; crypto_alt avg `-0.1877` n `237`; crypto_major avg `-0.0794` n `8`; equity avg `0.0169` n `154`; fx avg `-0.0013` n `6`; index avg `0.0132` n `27`; metal avg `-0.0071` n `20`; unknown avg `0.0286` n `1226`
- 4h: commodity avg `-0.1189` n `13`; crypto_alt avg `-0.0105` n `237`; crypto_major avg `-0.1426` n `8`; equity avg `-0.0642` n `154`; fx avg `-0.0306` n `6`; index avg `0.0159` n `27`; metal avg `-0.0116` n `20`; unknown avg `8.6448` n `1124`
- 24h: commodity avg `-0.0508` n `13`; crypto_alt avg `-0.5836` n `237`; crypto_major avg `-0.3455` n `8`; equity avg `0.5259` n `153`; fx avg `-0.0062` n `6`; index avg `-0.1355` n `27`; metal avg `-0.1218` n `20`; unknown avg `710.7262` n `980`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2192`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1823`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
