# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T10:07:27.215831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `13`; crypto_alt avg `-0.0159` n `237`; crypto_major avg `0.0195` n `8`; equity avg `0.012` n `152`; fx avg `0.0203` n `6`; index avg `0.0083` n `26`; metal avg `-0.0004` n `20`; unknown avg `-0.0397` n `1229`
- 1h: commodity avg `0.0027` n `13`; crypto_alt avg `0.2327` n `237`; crypto_major avg `-0.0516` n `8`; equity avg `0.0327` n `152`; fx avg `-0.0012` n `6`; index avg `0.0033` n `26`; metal avg `-0.0071` n `20`; unknown avg `10.0356` n `1203`
- 4h: commodity avg `0.0042` n `13`; crypto_alt avg `-0.7235` n `237`; crypto_major avg `-0.5928` n `8`; equity avg `-0.1733` n `152`; fx avg `0.0268` n `6`; index avg `-0.0022` n `26`; metal avg `0.0072` n `20`; unknown avg `11.0249` n `1183`
- 24h: commodity avg `0.0007` n `13`; crypto_alt avg `-1.6201` n `237`; crypto_major avg `-0.054` n `8`; equity avg `0.0259` n `152`; fx avg `-0.0125` n `6`; index avg `0.0309` n `26`; metal avg `-0.0515` n `20`; unknown avg `10.859` n `1048`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1962`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
