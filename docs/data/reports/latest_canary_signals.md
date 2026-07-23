# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T10:22:32.737269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.086` n `12`; crypto_alt avg `-0.0052` n `230`; crypto_major avg `0.0143` n `8`; equity avg `0.0035` n `98`; fx avg `-0.0011` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0116` n `20`; unknown avg `-0.0117` n `773`
- 1h: commodity avg `0.0107` n `12`; crypto_alt avg `-0.1087` n `230`; crypto_major avg `-0.0835` n `8`; equity avg `-0.1923` n `98`; fx avg `-0.0124` n `6`; index avg `-0.0174` n `25`; metal avg `-0.0755` n `20`; unknown avg `-0.0209` n `773`
- 4h: commodity avg `0.2956` n `12`; crypto_alt avg `0.0453` n `230`; crypto_major avg `0.0905` n `8`; equity avg `0.176` n `98`; fx avg `0.0037` n `6`; index avg `-0.0172` n `25`; metal avg `-0.3664` n `20`; unknown avg `-0.0281` n `773`
- 24h: commodity avg `0.8137` n `12`; crypto_alt avg `-0.2712` n `230`; crypto_major avg `-0.1584` n `8`; equity avg `0.4769` n `98`; fx avg `-0.0992` n `6`; index avg `0.1061` n `25`; metal avg `-0.4271` n `20`; unknown avg `11.4796` n `741`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0818`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
