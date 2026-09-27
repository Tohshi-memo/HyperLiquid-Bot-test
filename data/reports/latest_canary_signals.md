# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T12:22:29.043573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `-0.0545` n `234`; crypto_major avg `-0.0179` n `8`; equity avg `0.0176` n `141`; fx avg `0.0039` n `6`; index avg `-0.0012` n `26`; metal avg `0.0023` n `20`; unknown avg `0.1825` n `962`
- 1h: commodity avg `0.0064` n `12`; crypto_alt avg `0.1681` n `234`; crypto_major avg `0.2169` n `8`; equity avg `0.0185` n `141`; fx avg `0.0036` n `6`; index avg `-0.0124` n `26`; metal avg `-0.0002` n `20`; unknown avg `2.2088` n `954`
- 4h: commodity avg `0.0339` n `12`; crypto_alt avg `-0.1071` n `234`; crypto_major avg `0.0938` n `8`; equity avg `0.0461` n `141`; fx avg `-0.0041` n `6`; index avg `-0.0095` n `26`; metal avg `-0.0076` n `20`; unknown avg `1.9405` n `953`
- 24h: commodity avg `0.0502` n `12`; crypto_alt avg `0.7004` n `234`; crypto_major avg `0.8701` n `8`; equity avg `0.3657` n `141`; fx avg `-0.0303` n `6`; index avg `0.027` n `26`; metal avg `-0.0051` n `20`; unknown avg `61.4277` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
