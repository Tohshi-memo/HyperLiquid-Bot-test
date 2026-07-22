# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T23:37:25.049839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `12`; crypto_alt avg `0.0971` n `230`; crypto_major avg `0.0982` n `8`; equity avg `0.1367` n `98`; fx avg `0.0046` n `6`; index avg `0.0409` n `25`; metal avg `0.0191` n `20`; unknown avg `-0.0229` n `773`
- 1h: commodity avg `-0.0446` n `12`; crypto_alt avg `-0.1614` n `230`; crypto_major avg `0.0353` n `8`; equity avg `0.0169` n `98`; fx avg `0.0157` n `6`; index avg `0.0163` n `25`; metal avg `0.0127` n `20`; unknown avg `0.2272` n `773`
- 4h: commodity avg `0.1928` n `12`; crypto_alt avg `-0.1071` n `230`; crypto_major avg `0.0307` n `8`; equity avg `0.0347` n `98`; fx avg `-0.0085` n `6`; index avg `-0.0256` n `25`; metal avg `-0.1086` n `20`; unknown avg `0.1426` n `773`
- 24h: commodity avg `0.6739` n `12`; crypto_alt avg `-0.5987` n `230`; crypto_major avg `-0.5737` n `8`; equity avg `-1.2406` n `98`; fx avg `-0.0467` n `6`; index avg `-0.1738` n `25`; metal avg `0.1599` n `20`; unknown avg `1.6844` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0951`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0807`, n `666`, weak_sample_signal
