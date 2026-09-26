# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T09:52:27.890538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0119` n `12`; crypto_alt avg `0.1594` n `234`; crypto_major avg `0.0139` n `8`; equity avg `0.002` n `141`; fx avg `0.0006` n `6`; index avg `-0.0021` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.8014` n `961`
- 1h: commodity avg `0.0028` n `12`; crypto_alt avg `-0.288` n `234`; crypto_major avg `-0.3982` n `8`; equity avg `-0.0417` n `141`; fx avg `0.0269` n `6`; index avg `-0.0011` n `26`; metal avg `-0.0017` n `20`; unknown avg `1.0138` n `959`
- 4h: commodity avg `-0.0522` n `12`; crypto_alt avg `0.4752` n `234`; crypto_major avg `-0.2506` n `8`; equity avg `-0.0175` n `141`; fx avg `0.015` n `6`; index avg `-0.0025` n `26`; metal avg `-0.0082` n `20`; unknown avg `-0.0529` n `919`
- 24h: commodity avg `0.0639` n `12`; crypto_alt avg `1.9984` n `234`; crypto_major avg `-0.3811` n `8`; equity avg `-0.891` n `141`; fx avg `-0.0622` n `6`; index avg `0.0055` n `26`; metal avg `0.0548` n `20`; unknown avg `1121.296` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
