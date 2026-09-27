# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T02:37:27.980304+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `-0.0917` n `234`; crypto_major avg `-0.1004` n `8`; equity avg `0.0026` n `141`; fx avg `0.001` n `6`; index avg `0.0019` n `26`; metal avg `-0.0001` n `20`; unknown avg `3.0087` n `957`
- 1h: commodity avg `0.0078` n `12`; crypto_alt avg `0.2305` n `234`; crypto_major avg `0.2959` n `8`; equity avg `0.0792` n `141`; fx avg `0.001` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0005` n `20`; unknown avg `1.5012` n `955`
- 4h: commodity avg `-0.0802` n `12`; crypto_alt avg `0.3066` n `234`; crypto_major avg `0.3495` n `8`; equity avg `0.106` n `141`; fx avg `0.0024` n `6`; index avg `0.0021` n `26`; metal avg `0.0023` n `20`; unknown avg `0.5313` n `947`
- 24h: commodity avg `-0.0736` n `12`; crypto_alt avg `0.7848` n `234`; crypto_major avg `-0.421` n `8`; equity avg `0.2459` n `141`; fx avg `0.0112` n `6`; index avg `-0.01` n `26`; metal avg `-0.0064` n `20`; unknown avg `4.4808` n `881`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
