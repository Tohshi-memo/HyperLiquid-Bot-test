# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T12:07:32.521569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.1168` n `230`; crypto_major avg `-0.1482` n `8`; equity avg `-0.0394` n `96`; fx avg `0.0046` n `6`; index avg `-0.0089` n `25`; metal avg `-0.0036` n `20`; unknown avg `-0.0345` n `770`
- 1h: commodity avg `-0.0168` n `12`; crypto_alt avg `-0.4168` n `230`; crypto_major avg `-0.2813` n `8`; equity avg `-0.0852` n `96`; fx avg `-0.0085` n `6`; index avg `-0.0074` n `25`; metal avg `-0.0123` n `20`; unknown avg `-0.0387` n `770`
- 4h: commodity avg `0.003` n `12`; crypto_alt avg `-0.3609` n `230`; crypto_major avg `-0.2172` n `8`; equity avg `-0.1559` n `96`; fx avg `-0.0202` n `6`; index avg `0.0065` n `25`; metal avg `-0.0398` n `20`; unknown avg `-0.0512` n `770`
- 24h: commodity avg `0.1822` n `12`; crypto_alt avg `-0.0574` n `230`; crypto_major avg `0.7344` n `8`; equity avg `0.0999` n `96`; fx avg `-0.0082` n `6`; index avg `-0.043` n `25`; metal avg `-0.0849` n `20`; unknown avg `0.0997` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1152`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.114`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.096`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
