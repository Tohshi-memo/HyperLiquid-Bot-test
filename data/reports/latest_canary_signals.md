# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T08:22:25.966042+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `-0.2359` n `233`; crypto_major avg `-0.1627` n `8`; equity avg `-0.1337` n `136`; fx avg `0.0031` n `6`; index avg `-0.0206` n `27`; metal avg `0.0003` n `20`; unknown avg `2.0724` n `838`
- 1h: commodity avg `-0.0143` n `12`; crypto_alt avg `-0.461` n `233`; crypto_major avg `-0.3952` n `8`; equity avg `-0.2582` n `136`; fx avg `0.0029` n `6`; index avg `-0.0282` n `27`; metal avg `-0.0188` n `20`; unknown avg `0.8373` n `836`
- 4h: commodity avg `0.0475` n `12`; crypto_alt avg `-0.5225` n `233`; crypto_major avg `-0.609` n `8`; equity avg `-0.6587` n `136`; fx avg `-0.0078` n `6`; index avg `-0.0996` n `26`; metal avg `-0.0233` n `20`; unknown avg `51.5007` n `804`
- 24h: commodity avg `0.1541` n `12`; crypto_alt avg `-0.1281` n `233`; crypto_major avg `-0.8461` n `8`; equity avg `-1.0954` n `136`; fx avg `-0.0129` n `6`; index avg `-0.1589` n `26`; metal avg `0.0038` n `20`; unknown avg `0.8096` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0568`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0489`, n `668`, weak_sample_signal
