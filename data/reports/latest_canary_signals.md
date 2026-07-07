# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T13:22:27.236745+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1255` n `12`; crypto_alt avg `-0.1669` n `229`; crypto_major avg `-0.0879` n `8`; equity avg `-0.1571` n `91`; fx avg `-0.0069` n `6`; index avg `-0.0325` n `25`; metal avg `0.0243` n `20`; unknown avg `-0.009` n `763`
- 1h: commodity avg `0.1409` n `12`; crypto_alt avg `-0.6648` n `229`; crypto_major avg `-0.6668` n `8`; equity avg `-0.41` n `91`; fx avg `0.0128` n `6`; index avg `-0.0713` n `25`; metal avg `-0.0756` n `20`; unknown avg `0.02` n `763`
- 4h: commodity avg `-0.1756` n `12`; crypto_alt avg `0.0349` n `229`; crypto_major avg `0.0226` n `8`; equity avg `-0.3897` n `91`; fx avg `-0.0901` n `6`; index avg `-0.0388` n `25`; metal avg `0.3267` n `20`; unknown avg `-0.1619` n `761`
- 24h: commodity avg `0.2379` n `12`; crypto_alt avg `1.7166` n `229`; crypto_major avg `1.6938` n `8`; equity avg `-1.3394` n `90`; fx avg `-0.1926` n `6`; index avg `-0.3735` n `25`; metal avg `0.2368` n `20`; unknown avg `-0.2145` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0512`, n `668`, weak_sample_signal
