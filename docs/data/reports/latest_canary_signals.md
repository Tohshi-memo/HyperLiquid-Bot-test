# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T13:37:28.553046+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `0.0285` n `233`; crypto_major avg `0.0467` n `8`; equity avg `0.0084` n `136`; fx avg `-0.0055` n `6`; index avg `0.0004` n `26`; metal avg `0.0019` n `20`; unknown avg `-0.0672` n `838`
- 1h: commodity avg `0.0085` n `12`; crypto_alt avg `-0.2137` n `233`; crypto_major avg `-0.072` n `8`; equity avg `-0.0403` n `136`; fx avg `0.005` n `6`; index avg `0.0011` n `26`; metal avg `0.0014` n `20`; unknown avg `-0.0469` n `830`
- 4h: commodity avg `0.0202` n `12`; crypto_alt avg `0.1367` n `233`; crypto_major avg `0.2238` n `8`; equity avg `0.0313` n `136`; fx avg `-0.0082` n `6`; index avg `0.0016` n `26`; metal avg `0.0353` n `20`; unknown avg `0.5223` n `824`
- 24h: commodity avg `0.0043` n `12`; crypto_alt avg `1.3857` n `233`; crypto_major avg `0.6709` n `8`; equity avg `0.0464` n `136`; fx avg `0.0417` n `6`; index avg `0.0175` n `26`; metal avg `-0.2765` n `20`; unknown avg `9.6908` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
