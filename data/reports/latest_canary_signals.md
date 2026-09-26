# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T08:07:25.910118+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `12`; crypto_alt avg `-0.1435` n `234`; crypto_major avg `-0.0858` n `8`; equity avg `-0.004` n `141`; fx avg `-0.0052` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0044` n `20`; unknown avg `3.4746` n `943`
- 1h: commodity avg `0.032` n `12`; crypto_alt avg `-0.0007` n `234`; crypto_major avg `-0.0511` n `8`; equity avg `0.009` n `141`; fx avg `0.0138` n `6`; index avg `-0.0057` n `26`; metal avg `-0.01` n `20`; unknown avg `3.4481` n `943`
- 4h: commodity avg `-0.0212` n `12`; crypto_alt avg `0.398` n `234`; crypto_major avg `-0.2557` n `8`; equity avg `0.0251` n `141`; fx avg `0.0153` n `6`; index avg `-0.0117` n `26`; metal avg `-0.0053` n `20`; unknown avg `3.3233` n `919`
- 24h: commodity avg `-0.0644` n `12`; crypto_alt avg `3.138` n `234`; crypto_major avg `0.8122` n `8`; equity avg `-0.5833` n `141`; fx avg `-0.0681` n `6`; index avg `0.0682` n `26`; metal avg `0.1702` n `20`; unknown avg `1127.2467` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
