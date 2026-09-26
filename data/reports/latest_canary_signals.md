# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T07:07:32.499093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0633` n `12`; crypto_alt avg `0.2168` n `234`; crypto_major avg `0.1283` n `8`; equity avg `0.0062` n `141`; fx avg `-0.0012` n `6`; index avg `-0.0001` n `26`; metal avg `-0.0001` n `20`; unknown avg `0.1098` n `959`
- 1h: commodity avg `-0.0612` n `12`; crypto_alt avg `0.6233` n `234`; crypto_major avg `0.1446` n `8`; equity avg `0.0108` n `141`; fx avg `0.0109` n `6`; index avg `0.0022` n `26`; metal avg `0.0052` n `20`; unknown avg `4.2311` n `959`
- 4h: commodity avg `-0.046` n `12`; crypto_alt avg `0.6056` n `234`; crypto_major avg `-0.3467` n `8`; equity avg `0.0044` n `141`; fx avg `0.0011` n `6`; index avg `-0.0282` n `26`; metal avg `-0.003` n `20`; unknown avg `-0.2576` n `929`
- 24h: commodity avg `0.0155` n `12`; crypto_alt avg `3.576` n `234`; crypto_major avg `1.0272` n `8`; equity avg `-0.6715` n `141`; fx avg `-0.0781` n `6`; index avg `0.0505` n `26`; metal avg `0.1885` n `20`; unknown avg `1127.904` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
