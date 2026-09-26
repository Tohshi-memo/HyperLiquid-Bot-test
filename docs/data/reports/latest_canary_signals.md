# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T22:37:24.827452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `12`; crypto_alt avg `-0.0374` n `234`; crypto_major avg `-0.0346` n `8`; equity avg `0.0066` n `141`; fx avg `-0.005` n `6`; index avg `-0.0005` n `26`; metal avg `-0.0005` n `20`; unknown avg `2.4624` n `961`
- 1h: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.0943` n `234`; crypto_major avg `-0.0809` n `8`; equity avg `-0.0013` n `141`; fx avg `-0.01` n `6`; index avg `0.0045` n `26`; metal avg `-0.0075` n `20`; unknown avg `2.7976` n `935`
- 4h: commodity avg `0.0331` n `12`; crypto_alt avg `-0.6335` n `234`; crypto_major avg `-0.0659` n `8`; equity avg `0.0151` n `141`; fx avg `-0.0173` n `6`; index avg `-0.0031` n `26`; metal avg `0.0086` n `20`; unknown avg `162.5232` n `929`
- 24h: commodity avg `0.3115` n `12`; crypto_alt avg `0.4389` n `234`; crypto_major avg `-0.9679` n `8`; equity avg `-0.0203` n `141`; fx avg `0.0097` n `6`; index avg `-0.0554` n `26`; metal avg `-0.0184` n `20`; unknown avg `4.3979` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
