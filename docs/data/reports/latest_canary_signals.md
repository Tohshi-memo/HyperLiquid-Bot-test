# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T00:52:32.327451+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0093` n `12`; crypto_alt avg `0.0139` n `230`; crypto_major avg `0.089` n `8`; equity avg `0.0822` n `96`; fx avg `-0.0085` n `6`; index avg `0.0172` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.138` n `770`
- 1h: commodity avg `0.0257` n `12`; crypto_alt avg `-0.0064` n `230`; crypto_major avg `0.0879` n `8`; equity avg `0.1396` n `96`; fx avg `0.0386` n `6`; index avg `-0.0145` n `25`; metal avg `0.0127` n `20`; unknown avg `-0.2272` n `770`
- 4h: commodity avg `0.0294` n `12`; crypto_alt avg `0.2453` n `230`; crypto_major avg `0.3001` n `8`; equity avg `0.1789` n `96`; fx avg `0.0339` n `6`; index avg `-0.0064` n `25`; metal avg `0.0064` n `20`; unknown avg `0.1581` n `770`
- 24h: commodity avg `0.3526` n `12`; crypto_alt avg `-0.2563` n `230`; crypto_major avg `0.697` n `8`; equity avg `-0.1422` n `96`; fx avg `-0.0411` n `6`; index avg `0.0166` n `25`; metal avg `-0.0659` n `20`; unknown avg `0.0559` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
