# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T05:22:29.824095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `12`; crypto_alt avg `-0.0365` n `234`; crypto_major avg `-0.0677` n `8`; equity avg `-0.0345` n `141`; fx avg `-0.0049` n `6`; index avg `-0.0033` n `26`; metal avg `0.0005` n `20`; unknown avg `-0.093` n `961`
- 1h: commodity avg `-0.0168` n `12`; crypto_alt avg `-0.1039` n `234`; crypto_major avg `-0.1263` n `8`; equity avg `0.0336` n `141`; fx avg `-0.0015` n `6`; index avg `-0.0024` n `26`; metal avg `0.0002` n `20`; unknown avg `26.2972` n `959`
- 4h: commodity avg `-0.0868` n `12`; crypto_alt avg `-0.2836` n `234`; crypto_major avg `-0.5626` n `8`; equity avg `0.0715` n `141`; fx avg `0.0003` n `6`; index avg `0.0242` n `26`; metal avg `0.0067` n `20`; unknown avg `1.5069` n `952`
- 24h: commodity avg `-0.0289` n `12`; crypto_alt avg `3.2723` n `234`; crypto_major avg `1.0473` n `8`; equity avg `-0.3882` n `141`; fx avg `-0.1026` n `6`; index avg `0.12` n `26`; metal avg `0.3007` n `20`; unknown avg `1126.8336` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
