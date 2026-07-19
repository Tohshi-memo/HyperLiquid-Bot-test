# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T05:22:23.811828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `0.0304` n `230`; crypto_major avg `0.0296` n `8`; equity avg `-0.0037` n `96`; fx avg `0.0039` n `6`; index avg `0.0034` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.0022` n `770`
- 1h: commodity avg `-0.0041` n `12`; crypto_alt avg `0.178` n `230`; crypto_major avg `0.1861` n `8`; equity avg `0.03` n `96`; fx avg `-0.003` n `6`; index avg `-0.0` n `25`; metal avg `0.007` n `20`; unknown avg `3.2853` n `770`
- 4h: commodity avg `-0.0554` n `12`; crypto_alt avg `0.051` n `230`; crypto_major avg `0.1912` n `8`; equity avg `0.218` n `96`; fx avg `0.0069` n `6`; index avg `0.0081` n `25`; metal avg `0.0314` n `20`; unknown avg `0.4692` n `770`
- 24h: commodity avg `0.3241` n `12`; crypto_alt avg `0.169` n `230`; crypto_major avg `0.9559` n `8`; equity avg `-0.0556` n `96`; fx avg `-0.0246` n `6`; index avg `-0.0699` n `25`; metal avg `-0.0241` n `20`; unknown avg `0.0902` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
