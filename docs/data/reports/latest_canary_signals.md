# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T22:37:25.273585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `13`; crypto_alt avg `-0.064` n `236`; crypto_major avg `-0.0627` n `8`; equity avg `-0.0369` n `151`; fx avg `-0.0044` n `6`; index avg `0.0056` n `26`; metal avg `-0.0001` n `20`; unknown avg `0.5684` n `1193`
- 1h: commodity avg `-0.0405` n `13`; crypto_alt avg `0.0796` n `236`; crypto_major avg `0.105` n `8`; equity avg `-0.3164` n `151`; fx avg `-0.0065` n `6`; index avg `-0.0354` n `26`; metal avg `-0.0134` n `20`; unknown avg `1.827` n `1189`
- 4h: commodity avg `-0.0704` n `13`; crypto_alt avg `0.6111` n `236`; crypto_major avg `0.4735` n `8`; equity avg `-0.5591` n `151`; fx avg `0.006` n `6`; index avg `-0.0671` n `26`; metal avg `0.0613` n `20`; unknown avg `1.9417` n `1107`
- 24h: commodity avg `0.3663` n `13`; crypto_alt avg `-1.5362` n `236`; crypto_major avg `-1.3636` n `8`; equity avg `-4.1362` n `151`; fx avg `0.0154` n `6`; index avg `-0.6591` n `26`; metal avg `-0.0846` n `20`; unknown avg `39.7789` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1649`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1148`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.113`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0894`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0765`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0708`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0708`, n `666`, weak_sample_signal
