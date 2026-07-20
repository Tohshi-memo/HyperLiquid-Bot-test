# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T15:07:30.053401+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0606` n `12`; crypto_alt avg `0.2941` n `230`; crypto_major avg `0.4716` n `8`; equity avg `0.1182` n `98`; fx avg `-0.0351` n `6`; index avg `-0.0052` n `25`; metal avg `-0.0541` n `20`; unknown avg `-0.0419` n `770`
- 1h: commodity avg `-0.0879` n `12`; crypto_alt avg `0.2602` n `230`; crypto_major avg `0.4911` n `8`; equity avg `-0.3689` n `98`; fx avg `-0.0521` n `6`; index avg `-0.11` n `25`; metal avg `0.0344` n `20`; unknown avg `-0.1843` n `770`
- 4h: commodity avg `-0.0167` n `12`; crypto_alt avg `0.2554` n `230`; crypto_major avg `0.32` n `8`; equity avg `-0.6185` n `98`; fx avg `-0.0921` n `6`; index avg `-0.0847` n `25`; metal avg `-0.078` n `20`; unknown avg `0.1971` n `770`
- 24h: commodity avg `-0.6017` n `12`; crypto_alt avg `0.5706` n `230`; crypto_major avg `0.1349` n `8`; equity avg `0.1754` n `97`; fx avg `-0.1263` n `6`; index avg `0.0846` n `25`; metal avg `0.1605` n `20`; unknown avg `-0.0557` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1082`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1033`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0954`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0871`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0801`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
