# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T11:37:30.103869+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3366` n `12`; crypto_alt avg `0.4019` n `230`; crypto_major avg `0.7281` n `8`; equity avg `0.3389` n `98`; fx avg `-0.019` n `6`; index avg `0.0775` n `25`; metal avg `0.1132` n `20`; unknown avg `0.1328` n `770`
- 1h: commodity avg `-0.3555` n `12`; crypto_alt avg `0.4297` n `230`; crypto_major avg `0.7685` n `8`; equity avg `0.5049` n `98`; fx avg `-0.0351` n `6`; index avg `0.1454` n `25`; metal avg `0.131` n `20`; unknown avg `0.0933` n `770`
- 4h: commodity avg `-0.6034` n `12`; crypto_alt avg `0.9793` n `230`; crypto_major avg `1.1506` n `8`; equity avg `0.9589` n `98`; fx avg `-0.041` n `6`; index avg `0.2367` n `25`; metal avg `0.1433` n `20`; unknown avg `0.2204` n `763`
- 24h: commodity avg `-0.8822` n `12`; crypto_alt avg `0.7615` n `230`; crypto_major avg `0.4492` n `8`; equity avg `1.1112` n `97`; fx avg `-0.057` n `6`; index avg `0.2506` n `25`; metal avg `0.3511` n `20`; unknown avg `-0.009` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1091`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.104`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0907`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0745`, n `666`, weak_sample_signal
