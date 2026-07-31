# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T22:39:58.233896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `-0.0213` n `230`; crypto_major avg `-0.0227` n `8`; equity avg `0.0778` n `102`; fx avg `-0.0126` n `6`; index avg `0.0202` n `25`; metal avg `0.0093` n `20`; unknown avg `3.435` n `781`
- 1h: commodity avg `-0.1256` n `12`; crypto_alt avg `0.0339` n `230`; crypto_major avg `0.0083` n `8`; equity avg `-0.1109` n `102`; fx avg `0.0135` n `6`; index avg `0.0133` n `25`; metal avg `0.0269` n `20`; unknown avg `6.2341` n `781`
- 4h: commodity avg `0.6261` n `12`; crypto_alt avg `-0.199` n `230`; crypto_major avg `-0.1625` n `8`; equity avg `-0.939` n `102`; fx avg `-0.0667` n `6`; index avg `-0.119` n `25`; metal avg `-0.0813` n `20`; unknown avg `1.9824` n `780`
- 24h: commodity avg `0.7311` n `12`; crypto_alt avg `-0.8031` n `230`; crypto_major avg `-2.4853` n `8`; equity avg `-1.6507` n `102`; fx avg `0.1049` n `6`; index avg `-0.0014` n `25`; metal avg `-0.4209` n `20`; unknown avg `2.5074` n `747`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
