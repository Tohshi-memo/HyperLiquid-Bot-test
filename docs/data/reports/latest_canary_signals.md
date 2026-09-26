# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T03:22:29.757994+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `-0.2885` n `234`; crypto_major avg `-0.1575` n `8`; equity avg `-0.0174` n `141`; fx avg `0.0081` n `6`; index avg `-0.0222` n `26`; metal avg `-0.0047` n `20`; unknown avg `-0.2091` n `961`
- 1h: commodity avg `0.0145` n `12`; crypto_alt avg `-0.5794` n `234`; crypto_major avg `-0.3999` n `8`; equity avg `-0.0254` n `141`; fx avg `0.0121` n `6`; index avg `0.0061` n `26`; metal avg `-0.0073` n `20`; unknown avg `-0.1892` n `959`
- 4h: commodity avg `0.2954` n `12`; crypto_alt avg `-0.8549` n `234`; crypto_major avg `-0.5012` n `8`; equity avg `-0.1693` n `141`; fx avg `0.008` n `6`; index avg `-0.0461` n `26`; metal avg `-0.0188` n `20`; unknown avg `-0.0572` n `952`
- 24h: commodity avg `0.1342` n `12`; crypto_alt avg `3.2695` n `234`; crypto_major avg `1.2079` n `8`; equity avg `-0.3874` n `141`; fx avg `-0.1154` n `6`; index avg `0.1247` n `26`; metal avg `0.149` n `20`; unknown avg `1126.4922` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
