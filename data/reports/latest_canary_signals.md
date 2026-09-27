# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T20:22:28.009816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0255` n `12`; crypto_alt avg `-0.1497` n `234`; crypto_major avg `-0.0901` n `8`; equity avg `-0.0018` n `141`; fx avg `0.0006` n `6`; index avg `0.0026` n `26`; metal avg `-0.002` n `20`; unknown avg `8.034` n `962`
- 1h: commodity avg `0.0331` n `12`; crypto_alt avg `-0.1493` n `234`; crypto_major avg `-0.183` n `8`; equity avg `0.0292` n `141`; fx avg `0.0004` n `6`; index avg `0.0067` n `26`; metal avg `-0.002` n `20`; unknown avg `7.4742` n `954`
- 4h: commodity avg `0.0297` n `12`; crypto_alt avg `0.6741` n `234`; crypto_major avg `0.1996` n `8`; equity avg `0.1433` n `141`; fx avg `-0.0062` n `6`; index avg `0.0105` n `26`; metal avg `0.0087` n `20`; unknown avg `3.5175` n `928`
- 24h: commodity avg `-0.1253` n `12`; crypto_alt avg `1.1823` n `234`; crypto_major avg `0.6258` n `8`; equity avg `0.4229` n `141`; fx avg `-0.0159` n `6`; index avg `0.0442` n `26`; metal avg `-0.0085` n `20`; unknown avg `8.4434` n `871`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
