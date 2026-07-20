# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T11:52:29.046865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0978` n `12`; crypto_alt avg `0.0002` n `230`; crypto_major avg `0.062` n `8`; equity avg `0.0028` n `98`; fx avg `0.0064` n `6`; index avg `-0.0221` n `25`; metal avg `-0.0275` n `20`; unknown avg `0.057` n `770`
- 1h: commodity avg `-0.2726` n `12`; crypto_alt avg `0.4615` n `230`; crypto_major avg `0.8298` n `8`; equity avg `0.4927` n `98`; fx avg `-0.0223` n `6`; index avg `0.1082` n `25`; metal avg `0.1036` n `20`; unknown avg `0.2565` n `770`
- 4h: commodity avg `-0.4081` n `12`; crypto_alt avg `0.7843` n `230`; crypto_major avg `1.0682` n `8`; equity avg `0.9693` n `98`; fx avg `-0.0309` n `6`; index avg `0.2156` n `25`; metal avg `0.0853` n `20`; unknown avg `0.231` n `769`
- 24h: commodity avg `-0.7755` n `12`; crypto_alt avg `0.9439` n `230`; crypto_major avg `0.6502` n `8`; equity avg `1.1296` n `97`; fx avg `-0.0402` n `6`; index avg `0.2286` n `25`; metal avg `0.3209` n `20`; unknown avg `0.0103` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1049`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1022`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0918`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0737`, n `666`, weak_sample_signal
