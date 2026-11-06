# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T01:37:32.032802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `13`; crypto_alt avg `0.3628` n `239`; crypto_major avg `0.2553` n `8`; equity avg `0.416` n `158`; fx avg `0.0217` n `6`; index avg `0.0571` n `27`; metal avg `0.0315` n `20`; unknown avg `0.2478` n `1256`
- 1h: commodity avg `0.0782` n `13`; crypto_alt avg `-0.1016` n `239`; crypto_major avg `-0.1577` n `8`; equity avg `-0.2942` n `158`; fx avg `-0.0078` n `6`; index avg `-0.0656` n `27`; metal avg `-0.1024` n `20`; unknown avg `24.3417` n `1254`
- 4h: commodity avg `0.0658` n `13`; crypto_alt avg `0.1044` n `239`; crypto_major avg `-0.157` n `8`; equity avg `0.5026` n `158`; fx avg `0.0159` n `6`; index avg `0.1001` n `27`; metal avg `-0.0141` n `20`; unknown avg `3.7269` n `1216`
- 24h: commodity avg `1.2042` n `13`; crypto_alt avg `-4.3546` n `239`; crypto_major avg `-5.2599` n `8`; equity avg `-6.4773` n `158`; fx avg `0.0601` n `6`; index avg `-0.9453` n `27`; metal avg `-0.2518` n `20`; unknown avg `231.5355` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2326`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1763`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
