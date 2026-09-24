# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T06:07:32.155685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `-0.0299` n `234`; crypto_major avg `-0.1069` n `8`; equity avg `-0.2029` n `141`; fx avg `-0.0041` n `6`; index avg `-0.0282` n `26`; metal avg `-0.0124` n `20`; unknown avg `0.0281` n `927`
- 1h: commodity avg `0.1737` n `12`; crypto_alt avg `-0.569` n `234`; crypto_major avg `-0.5279` n `8`; equity avg `-0.3562` n `141`; fx avg `0.0103` n `6`; index avg `-0.0592` n `26`; metal avg `-0.0571` n `20`; unknown avg `0.3753` n `927`
- 4h: commodity avg `0.0817` n `12`; crypto_alt avg `1.8571` n `234`; crypto_major avg `0.8992` n `8`; equity avg `-0.3281` n `141`; fx avg `0.0111` n `6`; index avg `-0.0616` n `26`; metal avg `0.124` n `20`; unknown avg `1.295` n `921`
- 24h: commodity avg `0.6927` n `12`; crypto_alt avg `-3.9993` n `234`; crypto_major avg `-3.7964` n `8`; equity avg `-2.0408` n `140`; fx avg `0.0664` n `6`; index avg `-0.4182` n `26`; metal avg `-0.5658` n `20`; unknown avg `585.614` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1557`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
