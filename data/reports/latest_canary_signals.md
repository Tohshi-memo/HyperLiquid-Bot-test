# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T22:07:19.781689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3651` n `12`; crypto_alt avg `-0.1265` n `228`; crypto_major avg `0.086` n `8`; equity avg `-0.0228` n `67`; fx avg `0.0072` n `6`; index avg `-0.136` n `23`; metal avg `0.0134` n `18`; unknown avg `-0.0185` n `405`
- 1h: commodity avg `-0.0181` n `12`; crypto_alt avg `-0.0822` n `228`; crypto_major avg `-0.0258` n `8`; equity avg `-0.002` n `67`; fx avg `-0.039` n `6`; index avg `-0.0482` n `23`; metal avg `-0.0138` n `18`; unknown avg `0.0758` n `405`
- 4h: commodity avg `0.0087` n `12`; crypto_alt avg `-0.8672` n `228`; crypto_major avg `-0.5539` n `8`; equity avg `-0.03` n `67`; fx avg `0.0325` n `6`; index avg `-0.0847` n `23`; metal avg `0.0361` n `18`; unknown avg `-0.4775` n `405`
- 24h: commodity avg `-0.4467` n `12`; crypto_alt avg `2.3697` n `228`; crypto_major avg `0.5353` n `8`; equity avg `0.9801` n `67`; fx avg `-0.0611` n `6`; index avg `0.6548` n `23`; metal avg `0.9676` n `18`; unknown avg `1.3323` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
