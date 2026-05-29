# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T10:07:21.499475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.049` n `12`; crypto_alt avg `-0.0421` n `228`; crypto_major avg `-0.0873` n `8`; equity avg `-0.1202` n `69`; fx avg `0.0064` n `6`; index avg `-0.0676` n `23`; metal avg `-0.0741` n `18`; unknown avg `-0.0186` n `417`
- 1h: commodity avg `-0.2514` n `12`; crypto_alt avg `0.1561` n `228`; crypto_major avg `0.0986` n `8`; equity avg `-0.0336` n `69`; fx avg `0.0167` n `6`; index avg `-0.0291` n `23`; metal avg `0.2517` n `18`; unknown avg `-0.1956` n `417`
- 4h: commodity avg `-0.0474` n `12`; crypto_alt avg `0.4002` n `228`; crypto_major avg `0.4056` n `8`; equity avg `-0.1728` n `69`; fx avg `0.0031` n `6`; index avg `-0.0879` n `23`; metal avg `-0.0176` n `18`; unknown avg `0.0916` n `417`
- 24h: commodity avg `0.3635` n `12`; crypto_alt avg `1.4561` n `228`; crypto_major avg `2.0232` n `8`; equity avg `3.348` n `69`; fx avg `0.1535` n `6`; index avg `1.2624` n `23`; metal avg `1.8102` n `18`; unknown avg `1.0636` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
