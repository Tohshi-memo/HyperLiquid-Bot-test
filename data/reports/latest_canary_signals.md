# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T15:19:24.978959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `0.2688` n `230`; crypto_major avg `0.3163` n `8`; equity avg `0.1074` n `98`; fx avg `-0.0135` n `6`; index avg `0.0369` n `25`; metal avg `0.0362` n `20`; unknown avg `-0.0122` n `770`
- 1h: commodity avg `-0.0922` n `12`; crypto_alt avg `0.8528` n `230`; crypto_major avg `1.1541` n `8`; equity avg `0.3448` n `98`; fx avg `-0.0649` n `6`; index avg `0.013` n `25`; metal avg `0.1376` n `20`; unknown avg `0.61` n `770`
- 4h: commodity avg `-0.0344` n `12`; crypto_alt avg `0.5205` n `230`; crypto_major avg `0.7229` n `8`; equity avg `-0.5178` n `98`; fx avg `-0.1044` n `6`; index avg `-0.0632` n `25`; metal avg `-0.027` n `20`; unknown avg `0.3908` n `770`
- 24h: commodity avg `-0.6039` n `12`; crypto_alt avg `0.8355` n `230`; crypto_major avg `0.5269` n `8`; equity avg `0.2891` n `97`; fx avg `-0.1406` n `6`; index avg `0.1212` n `25`; metal avg `0.1976` n `20`; unknown avg `-0.0279` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0944`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0863`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0821`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
