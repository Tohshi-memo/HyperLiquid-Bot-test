# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T19:41:29.921213+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0322` n `12`; crypto_alt avg `0.0474` n `230`; crypto_major avg `0.1305` n `8`; equity avg `-0.0596` n `113`; fx avg `0.0132` n `6`; index avg `-0.0064` n `25`; metal avg `-0.0004` n `20`; unknown avg `0.0254` n `785`
- 1h: commodity avg `-0.0655` n `12`; crypto_alt avg `0.1895` n `230`; crypto_major avg `0.4457` n `8`; equity avg `0.0912` n `113`; fx avg `0.0211` n `6`; index avg `0.0223` n `25`; metal avg `0.0999` n `20`; unknown avg `0.1756` n `785`
- 4h: commodity avg `0.1008` n `12`; crypto_alt avg `0.0635` n `230`; crypto_major avg `0.3382` n `8`; equity avg `-0.0965` n `113`; fx avg `0.0271` n `6`; index avg `0.007` n `25`; metal avg `0.2801` n `20`; unknown avg `-0.0605` n `785`
- 24h: commodity avg `1.1848` n `12`; crypto_alt avg `-0.8006` n `230`; crypto_major avg `-0.9763` n `8`; equity avg `-1.3788` n `113`; fx avg `0.2751` n `6`; index avg `-0.0749` n `25`; metal avg `0.1958` n `20`; unknown avg `103.6071` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1726`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
