# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T23:35:03.983458+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0247` n `12`; crypto_alt avg `-0.0` n `234`; crypto_major avg `0.0138` n `8`; equity avg `-0.0033` n `141`; fx avg `-0.0119` n `6`; index avg `-0.0008` n `26`; metal avg `0.0025` n `20`; unknown avg `1.9595` n `961`
- 1h: commodity avg `-0.011` n `12`; crypto_alt avg `0.2539` n `234`; crypto_major avg `0.2351` n `8`; equity avg `0.0283` n `141`; fx avg `-0.0099` n `6`; index avg `0.0003` n `26`; metal avg `0.0032` n `20`; unknown avg `0.4017` n `959`
- 4h: commodity avg `0.0458` n `12`; crypto_alt avg `-0.009` n `234`; crypto_major avg `0.3156` n `8`; equity avg `0.0637` n `141`; fx avg `-0.0308` n `6`; index avg `-0.0041` n `26`; metal avg `0.0049` n `20`; unknown avg `168.4678` n `929`
- 24h: commodity avg `0.3106` n `12`; crypto_alt avg `0.5646` n `234`; crypto_major avg `-0.6698` n `8`; equity avg `0.0174` n `141`; fx avg `-0.0021` n `6`; index avg `-0.0588` n `26`; metal avg `-0.014` n `20`; unknown avg `4.0879` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
