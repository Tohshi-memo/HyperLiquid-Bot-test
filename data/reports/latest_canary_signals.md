# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T02:07:24.461402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `12`; crypto_alt avg `0.0558` n `230`; crypto_major avg `0.1335` n `8`; equity avg `-0.0233` n `98`; fx avg `0.0005` n `6`; index avg `0.0223` n `25`; metal avg `-0.0249` n `20`; unknown avg `-0.0768` n `771`
- 1h: commodity avg `0.0374` n `12`; crypto_alt avg `-0.2262` n `230`; crypto_major avg `-0.152` n `8`; equity avg `-0.3202` n `98`; fx avg `0.0014` n `6`; index avg `0.0352` n `25`; metal avg `-0.0609` n `20`; unknown avg `-0.0288` n `771`
- 4h: commodity avg `-0.0624` n `12`; crypto_alt avg `0.2473` n `230`; crypto_major avg `0.2852` n `8`; equity avg `0.2589` n `98`; fx avg `0.0589` n `6`; index avg `0.1856` n `25`; metal avg `0.1026` n `20`; unknown avg `-0.5296` n `770`
- 24h: commodity avg `-0.3697` n `12`; crypto_alt avg `1.222` n `230`; crypto_major avg `1.0281` n `8`; equity avg `-0.0959` n `98`; fx avg `-0.0937` n `6`; index avg `0.0722` n `25`; metal avg `0.1388` n `20`; unknown avg `-0.1091` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0874`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0744`, n `666`, weak_sample_signal
