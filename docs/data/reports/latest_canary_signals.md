# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T04:52:23.788802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `-0.0822` n `230`; crypto_major avg `-0.0544` n `8`; equity avg `-0.0444` n `96`; fx avg `0.0027` n `6`; index avg `-0.0019` n `25`; metal avg `0.0014` n `20`; unknown avg `-0.0675` n `770`
- 1h: commodity avg `-0.0399` n `12`; crypto_alt avg `-0.0072` n `230`; crypto_major avg `0.0523` n `8`; equity avg `0.0739` n `96`; fx avg `-0.0121` n `6`; index avg `-0.012` n `25`; metal avg `-0.005` n `20`; unknown avg `0.6458` n `770`
- 4h: commodity avg `-0.0722` n `12`; crypto_alt avg `-0.0783` n `230`; crypto_major avg `0.1057` n `8`; equity avg `0.0941` n `96`; fx avg `0.0016` n `6`; index avg `-0.0096` n `25`; metal avg `0.0423` n `20`; unknown avg `-0.0926` n `770`
- 24h: commodity avg `0.329` n `12`; crypto_alt avg `0.0386` n `230`; crypto_major avg `0.9107` n `8`; equity avg `-0.0585` n `96`; fx avg `-0.0363` n `6`; index avg `-0.0501` n `25`; metal avg `-0.0125` n `20`; unknown avg `0.0706` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
