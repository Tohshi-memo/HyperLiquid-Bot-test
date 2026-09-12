# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T11:22:28.245005+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.46` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0165` n `12`; crypto_alt avg `-0.1042` n `233`; crypto_major avg `-0.0505` n `8`; equity avg `-0.0016` n `136`; fx avg `0.0006` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.0656` n `838`
- 1h: commodity avg `-0.0214` n `12`; crypto_alt avg `-0.0738` n `233`; crypto_major avg `-0.0251` n `8`; equity avg `-0.0009` n `136`; fx avg `-0.0032` n `6`; index avg `-0.0029` n `26`; metal avg `-0.0038` n `20`; unknown avg `0.8784` n `836`
- 4h: commodity avg `0.065` n `12`; crypto_alt avg `0.034` n `233`; crypto_major avg `0.3262` n `8`; equity avg `0.0269` n `136`; fx avg `-0.008` n `6`; index avg `-0.0004` n `26`; metal avg `0.0048` n `20`; unknown avg `0.8424` n `830`
- 24h: commodity avg `-0.0283` n `12`; crypto_alt avg `3.0443` n `233`; crypto_major avg `2.2018` n `8`; equity avg `0.3028` n `136`; fx avg `-0.0456` n `6`; index avg `0.1347` n `26`; metal avg `0.027` n `20`; unknown avg `1.179` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
