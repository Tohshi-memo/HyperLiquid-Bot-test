# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T13:52:30.540025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0389` n `12`; crypto_alt avg `-0.3868` n `230`; crypto_major avg `-0.298` n `8`; equity avg `-0.5717` n `98`; fx avg `-0.0135` n `6`; index avg `-0.0625` n `25`; metal avg `0.0412` n `20`; unknown avg `0.1049` n `770`
- 1h: commodity avg `-0.1691` n `12`; crypto_alt avg `-0.2146` n `230`; crypto_major avg `-0.2299` n `8`; equity avg `-0.2427` n `98`; fx avg `-0.0287` n `6`; index avg `0.0569` n `25`; metal avg `0.063` n `20`; unknown avg `0.1054` n `770`
- 4h: commodity avg `0.066` n `12`; crypto_alt avg `0.136` n `230`; crypto_major avg `0.2431` n `8`; equity avg `-0.038` n `98`; fx avg `-0.0419` n `6`; index avg `0.0789` n `25`; metal avg `-0.0586` n `20`; unknown avg `0.395` n `770`
- 24h: commodity avg `-0.5546` n `12`; crypto_alt avg `0.4214` n `230`; crypto_major avg `0.0094` n `8`; equity avg `0.5219` n `97`; fx avg `-0.084` n `6`; index avg `0.2289` n `25`; metal avg `0.1893` n `20`; unknown avg `-0.0001` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1092`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1078`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1009`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0889`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0779`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
