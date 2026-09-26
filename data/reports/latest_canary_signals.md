# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T19:07:30.165480+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `0.1482` n `234`; crypto_major avg `0.1366` n `8`; equity avg `-0.0017` n `141`; fx avg `0.0015` n `6`; index avg `0.0005` n `26`; metal avg `0.0025` n `20`; unknown avg `0.8543` n `959`
- 1h: commodity avg `0.0054` n `12`; crypto_alt avg `-0.4286` n `234`; crypto_major avg `-0.2129` n `8`; equity avg `-0.0547` n `141`; fx avg `0.0018` n `6`; index avg `-0.0105` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.1387` n `959`
- 4h: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.5128` n `234`; crypto_major avg `-0.3389` n `8`; equity avg `-0.047` n `141`; fx avg `0.0041` n `6`; index avg `-0.0125` n `26`; metal avg `-0.0044` n `20`; unknown avg `4.1634` n `945`
- 24h: commodity avg `0.365` n `12`; crypto_alt avg `1.556` n `234`; crypto_major avg `-0.5728` n `8`; equity avg `-0.1445` n `141`; fx avg `0.0285` n `6`; index avg `-0.0313` n `26`; metal avg `-0.068` n `20`; unknown avg `3.2853` n `814`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
