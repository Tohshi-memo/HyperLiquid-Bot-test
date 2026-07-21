# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T01:22:29.118038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `-0.168` n `230`; crypto_major avg `-0.1572` n `8`; equity avg `0.0138` n `98`; fx avg `0.0023` n `6`; index avg `0.0004` n `25`; metal avg `-0.0004` n `20`; unknown avg `0.084` n `771`
- 1h: commodity avg `-0.0658` n `12`; crypto_alt avg `0.0788` n `230`; crypto_major avg `0.1223` n `8`; equity avg `0.6138` n `98`; fx avg `0.0217` n `6`; index avg `0.1625` n `25`; metal avg `0.135` n `20`; unknown avg `-0.1597` n `771`
- 4h: commodity avg `-0.0289` n `12`; crypto_alt avg `-0.0488` n `230`; crypto_major avg `-0.029` n `8`; equity avg `0.6111` n `98`; fx avg `0.0386` n `6`; index avg `0.1157` n `25`; metal avg `0.1372` n `20`; unknown avg `-0.4344` n `770`
- 24h: commodity avg `-0.3547` n `12`; crypto_alt avg `1.5332` n `230`; crypto_major avg `1.3039` n `8`; equity avg `0.0269` n `98`; fx avg `-0.1132` n `6`; index avg `0.0287` n `25`; metal avg `0.1897` n `20`; unknown avg `-0.0737` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0955`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0938`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0805`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
