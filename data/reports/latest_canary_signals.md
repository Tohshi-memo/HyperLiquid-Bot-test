# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T19:22:24.578388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `-0.1126` n `234`; crypto_major avg `-0.0441` n `8`; equity avg `0.0089` n `141`; fx avg `-0.0131` n `6`; index avg `0.0003` n `26`; metal avg `0.0035` n `20`; unknown avg `-0.052` n `961`
- 1h: commodity avg `0.0063` n `12`; crypto_alt avg `-0.4738` n `234`; crypto_major avg `-0.211` n `8`; equity avg `-0.0207` n `141`; fx avg `-0.006` n `6`; index avg `0.007` n `26`; metal avg `0.0058` n `20`; unknown avg `0.8755` n `959`
- 4h: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.8076` n `234`; crypto_major avg `-0.4496` n `8`; equity avg `-0.0561` n `141`; fx avg `-0.0111` n `6`; index avg `-0.0098` n `26`; metal avg `-0.0042` n `20`; unknown avg `3.252` n `945`
- 24h: commodity avg `0.3049` n `12`; crypto_alt avg `1.4641` n `234`; crypto_major avg `-0.6509` n `8`; equity avg `-0.0675` n `141`; fx avg `0.0061` n `6`; index avg `-0.0245` n `26`; metal avg `-0.045` n `20`; unknown avg `3.2443` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
