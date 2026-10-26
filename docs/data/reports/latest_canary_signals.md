# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T23:07:28.487091+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `13`; crypto_alt avg `-0.2756` n `237`; crypto_major avg `-0.2637` n `8`; equity avg `-0.2551` n `154`; fx avg `-0.0042` n `6`; index avg `-0.0469` n `27`; metal avg `-0.0335` n `20`; unknown avg `2.4532` n `1228`
- 1h: commodity avg `-0.0066` n `13`; crypto_alt avg `-0.373` n `237`; crypto_major avg `-0.2819` n `8`; equity avg `-0.2729` n `154`; fx avg `-0.0095` n `6`; index avg `-0.0467` n `27`; metal avg `-0.0395` n `20`; unknown avg `0.187` n `1218`
- 4h: commodity avg `-0.1873` n `13`; crypto_alt avg `-0.3605` n `237`; crypto_major avg `-0.4445` n `8`; equity avg `-0.2083` n `154`; fx avg `-0.0278` n `6`; index avg `-0.0139` n `27`; metal avg `0.0054` n `20`; unknown avg `8.8107` n `1116`
- 24h: commodity avg `-0.1528` n `13`; crypto_alt avg `-0.6405` n `237`; crypto_major avg `-0.4165` n `8`; equity avg `0.3469` n `153`; fx avg `-0.0097` n `6`; index avg `-0.1602` n `27`; metal avg `-0.0767` n `20`; unknown avg `715.6684` n `972`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1824`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
