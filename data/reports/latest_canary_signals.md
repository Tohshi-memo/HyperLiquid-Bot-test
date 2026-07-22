# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T21:37:27.524634+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0426` n `12`; crypto_alt avg `0.0423` n `230`; crypto_major avg `0.1504` n `8`; equity avg `-0.0166` n `98`; fx avg `-0.0092` n `6`; index avg `-0.0018` n `25`; metal avg `0.001` n `20`; unknown avg `0.004` n `773`
- 1h: commodity avg `0.0821` n `12`; crypto_alt avg `0.1088` n `230`; crypto_major avg `0.1217` n `8`; equity avg `0.1809` n `98`; fx avg `-0.0072` n `6`; index avg `-0.0137` n `25`; metal avg `-0.0159` n `20`; unknown avg `0.1656` n `773`
- 4h: commodity avg `0.0763` n `12`; crypto_alt avg `-0.2224` n `230`; crypto_major avg `-0.1258` n `8`; equity avg `-0.0433` n `98`; fx avg `-0.0035` n `6`; index avg `-0.0473` n `25`; metal avg `-0.0281` n `20`; unknown avg `0.1011` n `773`
- 24h: commodity avg `0.582` n `12`; crypto_alt avg `-0.3969` n `230`; crypto_major avg `-0.5395` n `8`; equity avg `-0.9239` n `98`; fx avg `-0.0333` n `6`; index avg `-0.1502` n `25`; metal avg `0.2689` n `20`; unknown avg `1.0362` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1669`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0864`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
