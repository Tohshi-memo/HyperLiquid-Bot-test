# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T03:52:31.610965+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `-0.0075` n `230`; crypto_major avg `-0.0765` n `8`; equity avg `0.1532` n `98`; fx avg `-0.0111` n `6`; index avg `0.0355` n `25`; metal avg `-0.0234` n `20`; unknown avg `0.0456` n `773`
- 1h: commodity avg `-0.001` n `12`; crypto_alt avg `-0.2128` n `230`; crypto_major avg `-0.15` n `8`; equity avg `0.2378` n `98`; fx avg `0.0008` n `6`; index avg `0.0519` n `25`; metal avg `0.009` n `20`; unknown avg `-0.0165` n `773`
- 4h: commodity avg `0.1798` n `12`; crypto_alt avg `-0.4384` n `230`; crypto_major avg `-0.4221` n `8`; equity avg `0.0083` n `98`; fx avg `-0.0707` n `6`; index avg `0.0293` n `25`; metal avg `0.1226` n `20`; unknown avg `-0.0188` n `773`
- 24h: commodity avg `0.7807` n `12`; crypto_alt avg `-0.8578` n `230`; crypto_major avg `-0.857` n `8`; equity avg `-0.4799` n `98`; fx avg `-0.1594` n `6`; index avg `-0.0553` n `25`; metal avg `-0.0906` n `20`; unknown avg `1.7909` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0925`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
