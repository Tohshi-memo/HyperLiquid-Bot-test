# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T08:37:29.042122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `12`; crypto_alt avg `-0.4202` n `230`; crypto_major avg `-0.3221` n `8`; equity avg `-0.2373` n `98`; fx avg `-0.0031` n `6`; index avg `-0.0236` n `25`; metal avg `-0.0113` n `20`; unknown avg `0.0021` n `769`
- 1h: commodity avg `-0.3109` n `12`; crypto_alt avg `-0.1928` n `230`; crypto_major avg `-0.1678` n `8`; equity avg `-0.087` n `98`; fx avg `-0.0072` n `6`; index avg `-0.0018` n `25`; metal avg `0.0564` n `20`; unknown avg `0.0451` n `763`
- 4h: commodity avg `-0.4909` n `12`; crypto_alt avg `-0.4058` n `230`; crypto_major avg `-0.8107` n `8`; equity avg `-0.3477` n `98`; fx avg `0.0096` n `6`; index avg `-0.0447` n `25`; metal avg `0.0977` n `20`; unknown avg `-0.1039` n `747`
- 24h: commodity avg `-0.5781` n `12`; crypto_alt avg `-0.4084` n `230`; crypto_major avg `-0.7241` n `8`; equity avg `-0.0602` n `97`; fx avg `-0.0194` n `6`; index avg `0.0195` n `25`; metal avg `0.2267` n `20`; unknown avg `0.0208` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0998`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0919`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.084`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0776`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
