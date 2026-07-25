# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T12:07:26.906068+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `0.045` n `230`; crypto_major avg `0.0106` n `8`; equity avg `0.0483` n `100`; fx avg `0.0015` n `6`; index avg `0.0056` n `25`; metal avg `-0.0023` n `20`; unknown avg `-0.002` n `774`
- 1h: commodity avg `-0.029` n `12`; crypto_alt avg `-0.1203` n `230`; crypto_major avg `-0.0409` n `8`; equity avg `0.0236` n `100`; fx avg `-0.0076` n `6`; index avg `-0.0063` n `25`; metal avg `-0.0094` n `20`; unknown avg `-0.0633` n `774`
- 4h: commodity avg `-0.0684` n `12`; crypto_alt avg `0.2139` n `230`; crypto_major avg `0.359` n `8`; equity avg `0.0247` n `100`; fx avg `-0.0146` n `6`; index avg `-0.0011` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.411` n `774`
- 24h: commodity avg `-0.1947` n `12`; crypto_alt avg `-1.2682` n `230`; crypto_major avg `-0.8661` n `8`; equity avg `-2.8378` n `100`; fx avg `-0.0067` n `6`; index avg `-0.2643` n `25`; metal avg `-0.1576` n `20`; unknown avg `13.175` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1183`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1021`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
