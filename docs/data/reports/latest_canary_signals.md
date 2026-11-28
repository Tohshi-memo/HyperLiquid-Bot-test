# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T23:37:32.993972+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0123` n `13`; crypto_alt avg `0.1656` n `239`; crypto_major avg `0.0308` n `8`; equity avg `0.0274` n `168`; fx avg `-0.0052` n `6`; index avg `0.0023` n `27`; metal avg `0.0227` n `20`; unknown avg `0.7968` n `1266`
- 1h: commodity avg `0.0077` n `13`; crypto_alt avg `0.1193` n `239`; crypto_major avg `0.0424` n `8`; equity avg `0.0453` n `168`; fx avg `0.0076` n `6`; index avg `0.0053` n `27`; metal avg `0.0059` n `20`; unknown avg `0.0574` n `1232`
- 4h: commodity avg `0.1409` n `13`; crypto_alt avg `0.4335` n `239`; crypto_major avg `0.4114` n `8`; equity avg `0.1973` n `168`; fx avg `0.0008` n `6`; index avg `0.0209` n `27`; metal avg `0.0341` n `20`; unknown avg `2.9939` n `1164`
- 24h: commodity avg `0.0854` n `13`; crypto_alt avg `-3.164` n `239`; crypto_major avg `-0.766` n `8`; equity avg `0.0799` n `168`; fx avg `0.0139` n `6`; index avg `0.0033` n `27`; metal avg `0.031` n `20`; unknown avg `0.0198` n `1063`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
