# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T08:07:24.923593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1079` n `12`; crypto_alt avg `0.0334` n `230`; crypto_major avg `-0.0337` n `8`; equity avg `0.069` n `98`; fx avg `0.0032` n `6`; index avg `0.0102` n `25`; metal avg `0.007` n `20`; unknown avg `0.1053` n `769`
- 1h: commodity avg `-0.4608` n `12`; crypto_alt avg `0.5959` n `230`; crypto_major avg `0.4038` n `8`; equity avg `0.3248` n `98`; fx avg `0.0178` n `6`; index avg `0.0633` n `25`; metal avg `0.2366` n `20`; unknown avg `0.177` n `763`
- 4h: commodity avg `-0.4079` n `12`; crypto_alt avg `0.0253` n `230`; crypto_major avg `-0.4649` n `8`; equity avg `-0.0176` n `98`; fx avg `0.011` n `6`; index avg `0.0305` n `25`; metal avg `0.09` n `20`; unknown avg `-0.0601` n `747`
- 24h: commodity avg `-0.4668` n `12`; crypto_alt avg `-0.0352` n `230`; crypto_major avg `-0.5151` n `8`; equity avg `0.0992` n `97`; fx avg `-0.0309` n `6`; index avg `0.0393` n `25`; metal avg `0.2055` n `20`; unknown avg `-0.0289` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1089`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1017`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0945`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0871`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0782`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
