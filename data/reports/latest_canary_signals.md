# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T15:07:32.024111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0352` n `12`; crypto_alt avg `-0.0263` n `233`; crypto_major avg `0.0199` n `8`; equity avg `0.0336` n `135`; fx avg `-0.0114` n `6`; index avg `0.0169` n `26`; metal avg `-0.0046` n `20`; unknown avg `0.0377` n `794`
- 1h: commodity avg `0.089` n `12`; crypto_alt avg `0.0225` n `233`; crypto_major avg `0.1934` n `8`; equity avg `0.6095` n `135`; fx avg `0.0276` n `6`; index avg `0.0915` n `26`; metal avg `-0.0413` n `20`; unknown avg `0.2912` n `766`
- 4h: commodity avg `0.4453` n `12`; crypto_alt avg `-0.5245` n `233`; crypto_major avg `-0.9517` n `8`; equity avg `-0.3047` n `135`; fx avg `0.0024` n `6`; index avg `-0.181` n `26`; metal avg `-0.3719` n `20`; unknown avg `-0.7383` n `760`
- 24h: commodity avg `0.3815` n `12`; crypto_alt avg `-4.2364` n `233`; crypto_major avg `-3.2695` n `8`; equity avg `-1.5974` n `135`; fx avg `0.0826` n `6`; index avg `-0.2515` n `26`; metal avg `-0.9693` n `20`; unknown avg `-0.8575` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
