# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T05:07:23.993661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0167` n `12`; crypto_alt avg `0.102` n `230`; crypto_major avg `0.0474` n `8`; equity avg `0.0427` n `96`; fx avg `0.0092` n `6`; index avg `0.0002` n `25`; metal avg `-0.0072` n `20`; unknown avg `1.0874` n `770`
- 1h: commodity avg `0.0008` n `12`; crypto_alt avg `0.1682` n `230`; crypto_major avg `0.1876` n `8`; equity avg `0.0152` n `96`; fx avg `-0.0075` n `6`; index avg `-0.0131` n `25`; metal avg `0.0067` n `20`; unknown avg `1.0848` n `770`
- 4h: commodity avg `-0.0387` n `12`; crypto_alt avg `0.089` n `230`; crypto_major avg `0.1964` n `8`; equity avg `0.1397` n `96`; fx avg `0.0084` n `6`; index avg `-0.0077` n `25`; metal avg `0.0318` n `20`; unknown avg `0.6952` n `770`
- 24h: commodity avg `0.3397` n `12`; crypto_alt avg `0.1269` n `230`; crypto_major avg `0.9564` n `8`; equity avg `-0.0494` n `96`; fx avg `-0.029` n `6`; index avg `-0.0547` n `25`; metal avg `-0.0228` n `20`; unknown avg `0.0819` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
