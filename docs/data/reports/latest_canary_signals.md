# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T03:52:27.657917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.0066` n `234`; crypto_major avg `-0.0214` n `8`; equity avg `-0.0086` n `141`; fx avg `0.0` n `6`; index avg `0.0008` n `26`; metal avg `-0.0002` n `20`; unknown avg `25.2571` n `961`
- 1h: commodity avg `-0.0013` n `12`; crypto_alt avg `-0.131` n `234`; crypto_major avg `-0.1949` n `8`; equity avg `-0.0043` n `141`; fx avg `-0.002` n `6`; index avg `0.005` n `26`; metal avg `-0.0055` n `20`; unknown avg `23.1461` n `959`
- 4h: commodity avg `-0.0276` n `12`; crypto_alt avg `-0.3726` n `234`; crypto_major avg `-0.1753` n `8`; equity avg `0.0586` n `141`; fx avg `-0.0037` n `6`; index avg `0.0071` n `26`; metal avg `-0.0143` n `20`; unknown avg `-0.3739` n `947`
- 24h: commodity avg `-0.0212` n `12`; crypto_alt avg `0.941` n `234`; crypto_major avg `-0.2968` n `8`; equity avg `0.2581` n `141`; fx avg `0.0064` n `6`; index avg `-0.0093` n `26`; metal avg `-0.0134` n `20`; unknown avg `4.3746` n `881`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
