# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T14:37:26.411731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.38` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0014` n `13`; crypto_alt avg `0.0793` n `239`; crypto_major avg `0.056` n `8`; equity avg `0.0676` n `168`; fx avg `-0.0024` n `6`; index avg `0.008` n `27`; metal avg `-0.0004` n `20`; unknown avg `0.9484` n `1267`
- 1h: commodity avg `0.0044` n `13`; crypto_alt avg `0.1265` n `239`; crypto_major avg `0.2108` n `8`; equity avg `0.036` n `168`; fx avg `0.0076` n `6`; index avg `0.0019` n `27`; metal avg `0.0253` n `20`; unknown avg `12.4138` n `1257`
- 4h: commodity avg `0.0015` n `13`; crypto_alt avg `-0.3932` n `239`; crypto_major avg `0.0993` n `8`; equity avg `-0.183` n `168`; fx avg `-0.0022` n `6`; index avg `-0.0167` n `27`; metal avg `-0.0062` n `20`; unknown avg `2.144` n `1243`
- 24h: commodity avg `-0.2616` n `13`; crypto_alt avg `-2.931` n `239`; crypto_major avg `-1.9911` n `8`; equity avg `1.424` n `168`; fx avg `-0.0753` n `6`; index avg `0.1611` n `27`; metal avg `0.2006` n `20`; unknown avg `191.4944` n `1092`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1487`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
