# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T09:37:29.117197+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0412` n `12`; crypto_alt avg `0.0798` n `230`; crypto_major avg `0.0198` n `8`; equity avg `-0.281` n `102`; fx avg `0.0358` n `6`; index avg `-0.0634` n `25`; metal avg `-0.0354` n `20`; unknown avg `-0.0117` n `780`
- 1h: commodity avg `0.2173` n `12`; crypto_alt avg `-0.3879` n `230`; crypto_major avg `-0.3409` n `8`; equity avg `-0.1179` n `102`; fx avg `0.0238` n `6`; index avg `0.0025` n `25`; metal avg `-0.1253` n `20`; unknown avg `-0.0683` n `780`
- 4h: commodity avg `0.4156` n `12`; crypto_alt avg `-0.3209` n `230`; crypto_major avg `-0.6856` n `8`; equity avg `-0.2214` n `102`; fx avg `-0.0738` n `6`; index avg `-0.0663` n `25`; metal avg `-0.222` n `20`; unknown avg `-0.0845` n `747`
- 24h: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.525` n `230`; crypto_major avg `-0.4028` n `8`; equity avg `8.0123` n `102`; fx avg `-0.186` n `6`; index avg `1.169` n `25`; metal avg `0.0619` n `20`; unknown avg `-0.0185` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
