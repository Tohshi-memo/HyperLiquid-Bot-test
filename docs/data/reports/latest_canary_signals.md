# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T16:50:00.200684+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `0.0054` n `229`; crypto_major avg `-0.0527` n `8`; equity avg `0.0087` n `88`; fx avg `-0.0012` n `6`; index avg `0.0005` n `25`; metal avg `0.0051` n `20`; unknown avg `0.0252` n `765`
- 1h: commodity avg `0.0189` n `12`; crypto_alt avg `-0.1034` n `229`; crypto_major avg `-0.2448` n `8`; equity avg `0.0184` n `88`; fx avg `0.0036` n `6`; index avg `0.0096` n `25`; metal avg `0.0015` n `20`; unknown avg `0.0375` n `713`
- 4h: commodity avg `0.0271` n `12`; crypto_alt avg `0.014` n `229`; crypto_major avg `0.1467` n `8`; equity avg `-0.0248` n `88`; fx avg `-0.037` n `6`; index avg `0.0345` n `25`; metal avg `-0.0092` n `20`; unknown avg `0.0996` n `695`
- 24h: commodity avg `0.0026` n `12`; crypto_alt avg `-1.6935` n `229`; crypto_major avg `-1.0424` n `8`; equity avg `0.2648` n `88`; fx avg `-0.077` n `6`; index avg `0.092` n `25`; metal avg `0.0615` n `20`; unknown avg `-0.0817` n `663`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
