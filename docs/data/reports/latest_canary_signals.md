# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T17:07:27.755666+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `12`; crypto_alt avg `-0.2783` n `234`; crypto_major avg `-0.1805` n `8`; equity avg `-0.0184` n `141`; fx avg `0.001` n `6`; index avg `0.0018` n `26`; metal avg `0.0036` n `20`; unknown avg `2.7954` n `959`
- 1h: commodity avg `-0.0074` n `12`; crypto_alt avg `-0.2993` n `234`; crypto_major avg `-0.2304` n `8`; equity avg `0.0001` n `141`; fx avg `0.0012` n `6`; index avg `0.0065` n `26`; metal avg `0.0068` n `20`; unknown avg `2.932` n `959`
- 4h: commodity avg `-0.0063` n `12`; crypto_alt avg `0.6988` n `234`; crypto_major avg `-0.001` n `8`; equity avg `0.083` n `141`; fx avg `-0.0146` n `6`; index avg `0.0292` n `26`; metal avg `0.0022` n `20`; unknown avg `2.9123` n `945`
- 24h: commodity avg `0.5091` n `12`; crypto_alt avg `2.7268` n `234`; crypto_major avg `-0.0234` n `8`; equity avg `-0.1271` n `141`; fx avg `0.0058` n `6`; index avg `0.0013` n `26`; metal avg `-0.0357` n `20`; unknown avg `2.2257` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
