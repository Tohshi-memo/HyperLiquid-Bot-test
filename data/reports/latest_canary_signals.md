# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T09:52:29.863703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `12`; crypto_alt avg `0.1371` n `230`; crypto_major avg `0.2208` n `8`; equity avg `0.0291` n `100`; fx avg `-0.0068` n `6`; index avg `0.0002` n `25`; metal avg `0.0036` n `20`; unknown avg `0.0173` n `774`
- 1h: commodity avg `0.023` n `12`; crypto_alt avg `0.3499` n `230`; crypto_major avg `0.4392` n `8`; equity avg `-0.0082` n `100`; fx avg `-0.0236` n `6`; index avg `0.011` n `25`; metal avg `0.0102` n `20`; unknown avg `0.4829` n `774`
- 4h: commodity avg `0.0607` n `12`; crypto_alt avg `-0.121` n `230`; crypto_major avg `0.2134` n `8`; equity avg `-0.0882` n `100`; fx avg `0.0194` n `6`; index avg `0.0159` n `25`; metal avg `0.0184` n `20`; unknown avg `-0.2025` n `758`
- 24h: commodity avg `0.1463` n `12`; crypto_alt avg `-1.6193` n `230`; crypto_major avg `-1.1937` n `8`; equity avg `-3.1128` n `100`; fx avg `-0.0181` n `6`; index avg `-0.2688` n `25`; metal avg `-0.1513` n `20`; unknown avg `13.1609` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.117`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1011`, n `666`, weak_sample_signal
