# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T11:22:29.121074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0094` n `12`; crypto_alt avg `0.0117` n `230`; crypto_major avg `-0.0848` n `8`; equity avg `0.0069` n `98`; fx avg `-0.0012` n `6`; index avg `0.0153` n `25`; metal avg `-0.015` n `20`; unknown avg `-0.0387` n `770`
- 1h: commodity avg `0.0334` n `12`; crypto_alt avg `0.0832` n `230`; crypto_major avg `0.0475` n `8`; equity avg `0.2343` n `98`; fx avg `-0.0078` n `6`; index avg `0.0671` n `25`; metal avg `-0.0097` n `20`; unknown avg `-0.008` n `770`
- 4h: commodity avg `-0.4045` n `12`; crypto_alt avg `0.7192` n `230`; crypto_major avg `0.5542` n `8`; equity avg `0.8658` n `98`; fx avg `-0.0208` n `6`; index avg `0.2072` n `25`; metal avg `0.2065` n `20`; unknown avg `0.1124` n `763`
- 24h: commodity avg `-0.4993` n `12`; crypto_alt avg `0.3133` n `230`; crypto_major avg `-0.3707` n `8`; equity avg `0.7132` n `97`; fx avg `-0.0451` n `6`; index avg `0.1704` n `25`; metal avg `0.2347` n `20`; unknown avg `-0.0821` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1068`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0975`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0878`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0783`, n `666`, weak_sample_signal
