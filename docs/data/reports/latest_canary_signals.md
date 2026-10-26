# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T13:07:33.556797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.082` n `13`; crypto_alt avg `-0.2253` n `237`; crypto_major avg `-0.2149` n `8`; equity avg `-0.1713` n `152`; fx avg `-0.0022` n `6`; index avg `-0.0209` n `26`; metal avg `-0.0311` n `20`; unknown avg `2.2119` n `1224`
- 1h: commodity avg `0.0644` n `13`; crypto_alt avg `-0.0366` n `237`; crypto_major avg `-0.1469` n `8`; equity avg `-0.221` n `152`; fx avg `-0.004` n `6`; index avg `-0.0503` n `26`; metal avg `-0.0677` n `20`; unknown avg `8.395` n `1226`
- 4h: commodity avg `0.181` n `13`; crypto_alt avg `0.2635` n `237`; crypto_major avg `0.2801` n `8`; equity avg `0.474` n `152`; fx avg `0.0009` n `6`; index avg `0.0319` n `26`; metal avg `-0.0187` n `20`; unknown avg `11.1321` n `1220`
- 24h: commodity avg `-0.2966` n `13`; crypto_alt avg `0.255` n `237`; crypto_major avg `0.1371` n `8`; equity avg `0.0119` n `152`; fx avg `0.0364` n `6`; index avg `0.0549` n `26`; metal avg `0.1266` n `20`; unknown avg `0.2135` n `963`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2506`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2077`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
