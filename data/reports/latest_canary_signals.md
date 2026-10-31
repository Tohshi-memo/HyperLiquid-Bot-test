# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T13:07:26.700693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.057` n `13`; crypto_alt avg `-0.3281` n `238`; crypto_major avg `-0.0991` n `8`; equity avg `-0.0326` n `156`; fx avg `-0.0039` n `6`; index avg `-0.0018` n `27`; metal avg `0.0018` n `20`; unknown avg `0.1793` n `1254`
- 1h: commodity avg `-0.0388` n `13`; crypto_alt avg `0.0416` n `238`; crypto_major avg `0.062` n `8`; equity avg `-0.0864` n `156`; fx avg `-0.016` n `6`; index avg `-0.0088` n `27`; metal avg `-0.0023` n `20`; unknown avg `0.221` n `1252`
- 4h: commodity avg `-0.0502` n `13`; crypto_alt avg `0.1046` n `238`; crypto_major avg `0.2728` n `8`; equity avg `-0.0721` n `156`; fx avg `-0.0045` n `6`; index avg `-0.015` n `27`; metal avg `0.0193` n `20`; unknown avg `206.4627` n `1216`
- 24h: commodity avg `-0.0994` n `13`; crypto_alt avg `0.6236` n `238`; crypto_major avg `-0.2438` n `8`; equity avg `-1.0181` n `156`; fx avg `-0.0249` n `6`; index avg `-0.1131` n `27`; metal avg `-0.072` n `20`; unknown avg `3.6957` n `1039`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
