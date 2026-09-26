# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T11:22:26.941510+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `0.0455` n `234`; crypto_major avg `0.0377` n `8`; equity avg `0.0052` n `141`; fx avg `-0.0102` n `6`; index avg `-0.001` n `26`; metal avg `0.0044` n `20`; unknown avg `1.0639` n `961`
- 1h: commodity avg `0.0021` n `12`; crypto_alt avg `0.2818` n `234`; crypto_major avg `0.0367` n `8`; equity avg `0.0293` n `141`; fx avg `-0.0033` n `6`; index avg `0.0034` n `26`; metal avg `0.0012` n `20`; unknown avg `7.8204` n `959`
- 4h: commodity avg `-0.0114` n `12`; crypto_alt avg `0.6331` n `234`; crypto_major avg `0.0393` n `8`; equity avg `0.0456` n `141`; fx avg `0.0098` n `6`; index avg `-0.0031` n `26`; metal avg `-0.0073` n `20`; unknown avg `3.8427` n `943`
- 24h: commodity avg `0.2077` n `12`; crypto_alt avg `1.8091` n `234`; crypto_major avg `-1.0745` n `8`; equity avg `-0.9549` n `141`; fx avg `-0.0245` n `6`; index avg `-0.0266` n `26`; metal avg `-0.0946` n `20`; unknown avg `1123.1716` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
