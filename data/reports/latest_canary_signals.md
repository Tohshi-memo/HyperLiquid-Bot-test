# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T15:37:34.567852+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `0.2602` n `234`; crypto_major avg `0.2654` n `8`; equity avg `0.0125` n `141`; fx avg `-0.0019` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0055` n `20`; unknown avg `0.463` n `961`
- 1h: commodity avg `-0.038` n `12`; crypto_alt avg `0.8974` n `234`; crypto_major avg `0.3894` n `8`; equity avg `0.0704` n `141`; fx avg `-0.0085` n `6`; index avg `0.0033` n `26`; metal avg `-0.0056` n `20`; unknown avg `15.1921` n `959`
- 4h: commodity avg `0.0555` n `12`; crypto_alt avg `0.9056` n `234`; crypto_major avg `0.2622` n `8`; equity avg `0.0922` n `141`; fx avg `-0.0142` n `6`; index avg `0.0053` n `26`; metal avg `-0.0004` n `20`; unknown avg `5.6634` n `949`
- 24h: commodity avg `0.0809` n `12`; crypto_alt avg `3.721` n `234`; crypto_major avg `0.5709` n `8`; equity avg `0.2055` n `141`; fx avg `-0.006` n `6`; index avg `0.0886` n `26`; metal avg `0.0414` n `20`; unknown avg `-0.3428` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
