# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T23:07:26.858870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.021` n `13`; crypto_alt avg `0.1607` n `239`; crypto_major avg `0.1191` n `8`; equity avg `-0.019` n `168`; fx avg `-0.001` n `6`; index avg `-0.0007` n `27`; metal avg `-0.0062` n `20`; unknown avg `0.1934` n `1251`
- 1h: commodity avg `0.0334` n `13`; crypto_alt avg `0.2481` n `239`; crypto_major avg `0.1815` n `8`; equity avg `-0.0038` n `168`; fx avg `-0.0089` n `6`; index avg `-0.0226` n `27`; metal avg `0.0238` n `20`; unknown avg `28.6299` n `1251`
- 4h: commodity avg `0.1601` n `13`; crypto_alt avg `0.2217` n `239`; crypto_major avg `-0.217` n `8`; equity avg `0.028` n `168`; fx avg `-0.0167` n `6`; index avg `0.0015` n `27`; metal avg `0.2019` n `20`; unknown avg `72.6711` n `1159`
- 24h: commodity avg `-0.4834` n `13`; crypto_alt avg `0.6514` n `239`; crypto_major avg `0.4211` n `8`; equity avg `3.4424` n `168`; fx avg `-0.1623` n `6`; index avg `0.3222` n `27`; metal avg `1.0609` n `20`; unknown avg `290.7588` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
