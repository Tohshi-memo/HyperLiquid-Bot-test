# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T13:22:32.758251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `-0.124` n `233`; crypto_major avg `-0.1387` n `8`; equity avg `-0.0388` n `136`; fx avg `0.0` n `6`; index avg `0.0001` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.1174` n `838`
- 1h: commodity avg `0.005` n `12`; crypto_alt avg `-0.1594` n `233`; crypto_major avg `-0.0591` n `8`; equity avg `-0.0395` n `136`; fx avg `0.007` n `6`; index avg `0.0014` n `26`; metal avg `-0.0032` n `20`; unknown avg `0.7447` n `824`
- 4h: commodity avg `0.0519` n `12`; crypto_alt avg `0.0468` n `233`; crypto_major avg `0.1652` n `8`; equity avg `0.0062` n `136`; fx avg `0.0037` n `6`; index avg `0.001` n `26`; metal avg `0.034` n `20`; unknown avg `0.2386` n `824`
- 24h: commodity avg `-0.0612` n `12`; crypto_alt avg `0.7811` n `233`; crypto_major avg `0.1138` n `8`; equity avg `-0.4286` n `136`; fx avg `0.0179` n `6`; index avg `-0.0066` n `26`; metal avg `-0.2065` n `20`; unknown avg `9.4823` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
