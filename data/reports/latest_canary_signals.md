# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T13:07:28.734253+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `0.0241` n `233`; crypto_major avg `0.1135` n `8`; equity avg `-0.0098` n `136`; fx avg `0.0072` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0012` n `20`; unknown avg `-0.0377` n `836`
- 1h: commodity avg `-0.0038` n `12`; crypto_alt avg `-0.0473` n `233`; crypto_major avg `0.0004` n `8`; equity avg `-0.0167` n `136`; fx avg `0.0081` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0005` n `20`; unknown avg `2.6206` n `824`
- 4h: commodity avg `0.0608` n `12`; crypto_alt avg `0.1578` n `233`; crypto_major avg `0.3189` n `8`; equity avg `0.0433` n `136`; fx avg `-0.0017` n `6`; index avg `-0.003` n `26`; metal avg `0.034` n `20`; unknown avg `0.7754` n `824`
- 24h: commodity avg `0.0179` n `12`; crypto_alt avg `1.0083` n `233`; crypto_major avg `0.332` n `8`; equity avg `-0.569` n `136`; fx avg `0.0439` n `6`; index avg `-0.0285` n `26`; metal avg `-0.184` n `20`; unknown avg `9.5019` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
