# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T09:07:18.772226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3389` n `12`; crypto_alt avg `0.1881` n `228`; crypto_major avg `-0.0063` n `8`; equity avg `0.053` n `69`; fx avg `-0.0117` n `6`; index avg `0.0617` n `23`; metal avg `0.2031` n `18`; unknown avg `0.006` n `417`
- 1h: commodity avg `-0.3514` n `12`; crypto_alt avg `0.1427` n `228`; crypto_major avg `-0.0585` n `8`; equity avg `-0.1477` n `69`; fx avg `-0.0289` n `6`; index avg `0.0038` n `23`; metal avg `-0.0858` n `18`; unknown avg `-0.0932` n `417`
- 4h: commodity avg `0.2253` n `12`; crypto_alt avg `0.318` n `228`; crypto_major avg `0.3092` n `8`; equity avg `-0.1603` n `69`; fx avg `-0.0026` n `6`; index avg `-0.0585` n `23`; metal avg `-0.2657` n `18`; unknown avg `1.0975` n `407`
- 24h: commodity avg `0.6975` n `12`; crypto_alt avg `1.7513` n `228`; crypto_major avg `2.2687` n `8`; equity avg `3.2896` n `69`; fx avg `0.1264` n `6`; index avg `1.2308` n `23`; metal avg `1.5851` n `18`; unknown avg `1.8086` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1676`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
