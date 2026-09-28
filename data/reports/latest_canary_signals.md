# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T02:07:30.834876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1604` n `12`; crypto_alt avg `-0.2057` n `234`; crypto_major avg `-0.1531` n `8`; equity avg `-0.1125` n `141`; fx avg `0.0133` n `6`; index avg `-0.031` n `26`; metal avg `-0.0326` n `20`; unknown avg `0.3795` n `960`
- 1h: commodity avg `0.1849` n `12`; crypto_alt avg `-1.3493` n `234`; crypto_major avg `-0.992` n `8`; equity avg `-0.6783` n `141`; fx avg `0.0587` n `6`; index avg `-0.0738` n `26`; metal avg `-0.125` n `20`; unknown avg `3.3573` n `950`
- 4h: commodity avg `0.0995` n `12`; crypto_alt avg `-0.6885` n `234`; crypto_major avg `-0.8823` n `8`; equity avg `-1.2243` n `141`; fx avg `0.1317` n `6`; index avg `-0.1141` n `26`; metal avg `-0.4959` n `20`; unknown avg `3.9514` n `918`
- 24h: commodity avg `-0.2906` n `12`; crypto_alt avg `-0.6194` n `234`; crypto_major avg `-1.3289` n `8`; equity avg `-1.1535` n `141`; fx avg `0.0998` n `6`; index avg `-0.1243` n `26`; metal avg `-0.6108` n `20`; unknown avg `13.4105` n `819`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
