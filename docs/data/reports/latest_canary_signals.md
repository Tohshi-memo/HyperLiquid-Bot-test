# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T06:52:28.686993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0268` n `13`; crypto_alt avg `0.0448` n `235`; crypto_major avg `-0.0097` n `8`; equity avg `0.0094` n `143`; fx avg `-0.0001` n `6`; index avg `-0.0032` n `26`; metal avg `0.0044` n `20`; unknown avg `0.1158` n `984`
- 1h: commodity avg `0.0209` n `13`; crypto_alt avg `-0.0915` n `235`; crypto_major avg `-0.0202` n `8`; equity avg `-0.0073` n `143`; fx avg `0.0033` n `6`; index avg `-0.0144` n `26`; metal avg `0.0062` n `20`; unknown avg `2.5812` n `960`
- 4h: commodity avg `-0.0425` n `13`; crypto_alt avg `0.15` n `235`; crypto_major avg `-0.0715` n `8`; equity avg `-0.0797` n `143`; fx avg `-0.0255` n `6`; index avg `-0.0175` n `26`; metal avg `0.0036` n `20`; unknown avg `-0.212` n `954`
- 24h: commodity avg `0.1463` n `13`; crypto_alt avg `-1.4159` n `235`; crypto_major avg `-1.8275` n `8`; equity avg `0.555` n `142`; fx avg `-0.0656` n `6`; index avg `0.2451` n `26`; metal avg `-0.2712` n `20`; unknown avg `-0.8816` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1703`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
