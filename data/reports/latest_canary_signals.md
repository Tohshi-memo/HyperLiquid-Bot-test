# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T02:07:32.459845+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0439` n `12`; crypto_alt avg `-0.1171` n `234`; crypto_major avg `-0.0385` n `8`; equity avg `0.0099` n `141`; fx avg `-0.0014` n `6`; index avg `0.0074` n `26`; metal avg `0.0041` n `20`; unknown avg `15.076` n `958`
- 1h: commodity avg `-0.0716` n `12`; crypto_alt avg `0.1458` n `234`; crypto_major avg `0.234` n `8`; equity avg `0.063` n `141`; fx avg `0.003` n `6`; index avg `0.0128` n `26`; metal avg `0.0085` n `20`; unknown avg `13.3023` n `958`
- 4h: commodity avg `0.2862` n `12`; crypto_alt avg `0.7359` n `234`; crypto_major avg `0.4941` n `8`; equity avg `-0.1313` n `141`; fx avg `0.0076` n `6`; index avg `-0.0458` n `26`; metal avg `-0.0071` n `20`; unknown avg `1.7184` n `936`
- 24h: commodity avg `0.0758` n `12`; crypto_alt avg `2.4566` n `234`; crypto_major avg `0.7793` n `8`; equity avg `-0.3605` n `141`; fx avg `-0.1607` n `6`; index avg `0.129` n `26`; metal avg `0.1039` n `20`; unknown avg `1126.1527` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
