# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T13:37:30.023495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0955` n `12`; crypto_alt avg `-0.0543` n `230`; crypto_major avg `-0.113` n `8`; equity avg `-0.2595` n `113`; fx avg `0.0053` n `6`; index avg `-0.0115` n `25`; metal avg `0.0033` n `20`; unknown avg `-0.1007` n `784`
- 1h: commodity avg `0.1109` n `12`; crypto_alt avg `-0.02` n `230`; crypto_major avg `-0.3068` n `8`; equity avg `-0.2435` n `113`; fx avg `0.0341` n `6`; index avg `-0.0012` n `25`; metal avg `-0.012` n `20`; unknown avg `-0.071` n `784`
- 4h: commodity avg `0.266` n `12`; crypto_alt avg `0.1025` n `230`; crypto_major avg `-0.2682` n `8`; equity avg `-0.998` n `113`; fx avg `0.0165` n `6`; index avg `-0.0935` n `25`; metal avg `-0.05` n `20`; unknown avg `-0.169` n `784`
- 24h: commodity avg `0.8169` n `12`; crypto_alt avg `0.5141` n `230`; crypto_major avg `-0.5257` n `8`; equity avg `-1.061` n `113`; fx avg `0.2499` n `6`; index avg `-0.0328` n `25`; metal avg `-0.1805` n `20`; unknown avg `56.9452` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1752`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1541`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
