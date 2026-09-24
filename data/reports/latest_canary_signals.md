# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T22:52:28.626312+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0171` n `12`; crypto_alt avg `-0.0352` n `234`; crypto_major avg `0.0448` n `8`; equity avg `0.0251` n `141`; fx avg `-0.001` n `6`; index avg `-0.0094` n `26`; metal avg `0.0069` n `20`; unknown avg `3.4687` n `946`
- 1h: commodity avg `-0.1563` n `12`; crypto_alt avg `-0.5177` n `234`; crypto_major avg `-0.4593` n `8`; equity avg `-0.024` n `141`; fx avg `-0.0102` n `6`; index avg `-0.0117` n `26`; metal avg `0.0191` n `20`; unknown avg `3.0429` n `904`
- 4h: commodity avg `-0.2227` n `12`; crypto_alt avg `-0.1427` n `234`; crypto_major avg `-0.637` n `8`; equity avg `-0.1881` n `141`; fx avg `-0.0394` n `6`; index avg `-0.048` n `26`; metal avg `-0.0692` n `20`; unknown avg `9.7317` n `829`
- 24h: commodity avg `0.6626` n `12`; crypto_alt avg `3.5525` n `234`; crypto_major avg `0.5967` n `8`; equity avg `-0.3701` n `141`; fx avg `0.0067` n `6`; index avg `-0.1322` n `26`; metal avg `-0.1268` n `20`; unknown avg `21.1907` n `815`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
