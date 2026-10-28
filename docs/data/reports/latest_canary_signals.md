# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T06:22:27.601790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.58` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.021` n `13`; crypto_alt avg `0.1834` n `238`; crypto_major avg `0.1188` n `8`; equity avg `0.0161` n `154`; fx avg `-0.0012` n `6`; index avg `-0.008` n `27`; metal avg `0.0056` n `20`; unknown avg `-0.0724` n `1236`
- 1h: commodity avg `0.0661` n `13`; crypto_alt avg `0.0378` n `238`; crypto_major avg `0.0474` n `8`; equity avg `-0.0357` n `154`; fx avg `-0.0404` n `6`; index avg `0.0036` n `27`; metal avg `-0.0103` n `20`; unknown avg `2.8762` n `1218`
- 4h: commodity avg `0.0453` n `13`; crypto_alt avg `-0.0749` n `238`; crypto_major avg `0.0123` n `8`; equity avg `0.5667` n `154`; fx avg `-0.0187` n `6`; index avg `0.0415` n `27`; metal avg `-0.0739` n `20`; unknown avg `0.6112` n `1198`
- 24h: commodity avg `0.0215` n `13`; crypto_alt avg `2.2379` n `237`; crypto_major avg `2.2839` n `8`; equity avg `3.8576` n `154`; fx avg `0.0555` n `6`; index avg `0.5383` n `27`; metal avg `0.3225` n `20`; unknown avg `92.2598` n `1016`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1626`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
