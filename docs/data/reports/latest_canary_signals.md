# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T05:52:19.210321+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0345` n `12`; crypto_alt avg `0.109` n `228`; crypto_major avg `0.2145` n `8`; equity avg `0.0596` n `69`; fx avg `0.0059` n `6`; index avg `-0.0227` n `23`; metal avg `-0.056` n `18`; unknown avg `0.2292` n `417`
- 1h: commodity avg `0.0539` n `12`; crypto_alt avg `0.3187` n `228`; crypto_major avg `0.2875` n `8`; equity avg `-0.004` n `69`; fx avg `0.0114` n `6`; index avg `0.028` n `23`; metal avg `-0.1344` n `18`; unknown avg `-0.1283` n `417`
- 4h: commodity avg `-0.082` n `12`; crypto_alt avg `-0.2141` n `228`; crypto_major avg `0.0783` n `8`; equity avg `0.4498` n `69`; fx avg `0.0151` n `6`; index avg `0.1674` n `23`; metal avg `-0.1846` n `18`; unknown avg `-0.076` n `417`
- 24h: commodity avg `-0.0267` n `12`; crypto_alt avg `1.5488` n `228`; crypto_major avg `2.0931` n `8`; equity avg `3.9241` n `69`; fx avg `0.1587` n `6`; index avg `1.448` n `23`; metal avg `1.7739` n `18`; unknown avg `0.8565` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
