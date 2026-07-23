# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T09:22:31.196579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1018` n `12`; crypto_alt avg `0.0012` n `230`; crypto_major avg `0.0103` n `8`; equity avg `-0.0415` n `98`; fx avg `-0.0042` n `6`; index avg `-0.0293` n `25`; metal avg `-0.0444` n `20`; unknown avg `-0.022` n `773`
- 1h: commodity avg `0.1313` n `12`; crypto_alt avg `0.1489` n `230`; crypto_major avg `0.2648` n `8`; equity avg `0.3184` n `98`; fx avg `-0.0128` n `6`; index avg `0.0285` n `25`; metal avg `0.0106` n `20`; unknown avg `-0.0089` n `773`
- 4h: commodity avg `0.3059` n `12`; crypto_alt avg `0.2086` n `230`; crypto_major avg `0.0773` n `8`; equity avg `0.2925` n `98`; fx avg `0.0141` n `6`; index avg `-0.0333` n `25`; metal avg `-0.319` n `20`; unknown avg `-0.0561` n `741`
- 24h: commodity avg `0.6638` n `12`; crypto_alt avg `-0.0718` n `230`; crypto_major avg `0.0292` n `8`; equity avg `0.6662` n `98`; fx avg `-0.0665` n `6`; index avg `0.1457` n `25`; metal avg `-0.3209` n `20`; unknown avg `11.505` n `741`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0846`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
