# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T18:07:32.066296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0357` n `12`; crypto_alt avg `-0.052` n `234`; crypto_major avg `0.011` n `8`; equity avg `-0.0075` n `141`; fx avg `-0.0035` n `6`; index avg `0.0007` n `26`; metal avg `0.0018` n `20`; unknown avg `0.4234` n `960`
- 1h: commodity avg `0.049` n `12`; crypto_alt avg `0.2789` n `234`; crypto_major avg `0.2359` n `8`; equity avg `0.0789` n `141`; fx avg `-0.0075` n `6`; index avg `0.0223` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.6381` n `960`
- 4h: commodity avg `-0.0997` n `12`; crypto_alt avg `0.0828` n `234`; crypto_major avg `-0.5476` n `8`; equity avg `0.0409` n `141`; fx avg `0.0069` n `6`; index avg `0.0248` n `26`; metal avg `0.0034` n `20`; unknown avg `5.333` n `954`
- 24h: commodity avg `-0.0973` n `12`; crypto_alt avg `-0.2431` n `234`; crypto_major avg `0.0323` n `8`; equity avg `0.3088` n `141`; fx avg `-0.0228` n `6`; index avg `0.0244` n `26`; metal avg `-0.0104` n `20`; unknown avg `92.5273` n `897`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
