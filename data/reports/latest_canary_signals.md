# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T14:22:26.814949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0173` n `12`; crypto_alt avg `0.0638` n `234`; crypto_major avg `0.1368` n `8`; equity avg `0.0362` n `141`; fx avg `-0.0042` n `6`; index avg `0.0013` n `26`; metal avg `0.0032` n `20`; unknown avg `0.0807` n `961`
- 1h: commodity avg `0.0522` n `12`; crypto_alt avg `0.2997` n `234`; crypto_major avg `0.1713` n `8`; equity avg `0.0139` n `141`; fx avg `0.0005` n `6`; index avg `0.0088` n `26`; metal avg `0.0035` n `20`; unknown avg `1.5288` n `959`
- 4h: commodity avg `0.0454` n `12`; crypto_alt avg `0.0508` n `234`; crypto_major avg `-0.0241` n `8`; equity avg `0.0543` n `141`; fx avg `0.0181` n `6`; index avg `0.0024` n `26`; metal avg `0.003` n `20`; unknown avg `1.9916` n `949`
- 24h: commodity avg `0.2278` n `12`; crypto_alt avg `2.6355` n `234`; crypto_major avg `-0.0923` n `8`; equity avg `0.4045` n `141`; fx avg `-0.0121` n `6`; index avg `0.135` n `26`; metal avg `0.2256` n `20`; unknown avg `2.3189` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
