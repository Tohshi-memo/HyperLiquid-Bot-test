# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T14:52:27.453846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0118` n `13`; crypto_alt avg `-0.0835` n `239`; crypto_major avg `-0.054` n `8`; equity avg `-0.0187` n `165`; fx avg `-0.0075` n `6`; index avg `-0.001` n `27`; metal avg `-0.0031` n `20`; unknown avg `8.6386` n `1265`
- 1h: commodity avg `0.1014` n `13`; crypto_alt avg `-0.1006` n `239`; crypto_major avg `0.0408` n `8`; equity avg `0.8497` n `165`; fx avg `-0.0042` n `6`; index avg `0.0352` n `27`; metal avg `-0.0425` n `20`; unknown avg `-0.4202` n `1263`
- 4h: commodity avg `0.2474` n `13`; crypto_alt avg `0.0976` n `239`; crypto_major avg `0.3854` n `8`; equity avg `0.435` n `165`; fx avg `-0.0484` n `6`; index avg `-0.0274` n `27`; metal avg `-0.2233` n `20`; unknown avg `8.5015` n `1257`
- 24h: commodity avg `0.387` n `13`; crypto_alt avg `0.6477` n `239`; crypto_major avg `1.1287` n `8`; equity avg `3.2924` n `165`; fx avg `0.018` n `6`; index avg `0.4392` n `27`; metal avg `-0.2416` n `20`; unknown avg `2.2086` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
