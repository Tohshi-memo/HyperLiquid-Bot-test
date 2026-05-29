# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T12:07:21.761207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.076` n `12`; crypto_alt avg `-0.1803` n `228`; crypto_major avg `-0.1175` n `8`; equity avg `-0.0653` n `69`; fx avg `-0.0046` n `6`; index avg `-0.0517` n `23`; metal avg `-0.1593` n `18`; unknown avg `0.0168` n `417`
- 1h: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.6726` n `228`; crypto_major avg `-0.484` n `8`; equity avg `-0.1324` n `69`; fx avg `-0.0087` n `6`; index avg `-0.0113` n `23`; metal avg `-0.1358` n `18`; unknown avg `0.8054` n `417`
- 4h: commodity avg `-0.551` n `12`; crypto_alt avg `-0.7309` n `228`; crypto_major avg `-0.5984` n `8`; equity avg `-0.3428` n `69`; fx avg `-0.0218` n `6`; index avg `0.117` n `23`; metal avg `0.1126` n `18`; unknown avg `-0.2432` n `417`
- 24h: commodity avg `-0.0939` n `12`; crypto_alt avg `1.3019` n `228`; crypto_major avg `1.7385` n `8`; equity avg `3.3019` n `69`; fx avg `0.1118` n `6`; index avg `1.427` n `23`; metal avg `2.2116` n `18`; unknown avg `1.9369` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
