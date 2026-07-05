# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T16:52:25.906294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0103` n `12`; crypto_alt avg `0.0112` n `229`; crypto_major avg `-0.0469` n `8`; equity avg `0.0091` n `88`; fx avg `-0.0012` n `6`; index avg `0.0004` n `25`; metal avg `0.0041` n `20`; unknown avg `0.0236` n `765`
- 1h: commodity avg `0.0205` n `12`; crypto_alt avg `-0.0976` n `229`; crypto_major avg `-0.2391` n `8`; equity avg `0.0188` n `88`; fx avg `0.0036` n `6`; index avg `0.0094` n `25`; metal avg `0.0004` n `20`; unknown avg `0.0351` n `713`
- 4h: commodity avg `0.0286` n `12`; crypto_alt avg `0.0198` n `229`; crypto_major avg `0.1525` n `8`; equity avg `-0.0244` n `88`; fx avg `-0.037` n `6`; index avg `0.0344` n `25`; metal avg `-0.0103` n `20`; unknown avg `0.0989` n `695`
- 24h: commodity avg `0.0041` n `12`; crypto_alt avg `-1.6875` n `229`; crypto_major avg `-1.0367` n `8`; equity avg `0.2652` n `88`; fx avg `-0.077` n `6`; index avg `0.0918` n `25`; metal avg `0.0604` n `20`; unknown avg `-0.0817` n `663`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
