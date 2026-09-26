# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T15:52:34.482460+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0352` n `12`; crypto_alt avg `-0.0097` n `234`; crypto_major avg `-0.0446` n `8`; equity avg `-0.0218` n `141`; fx avg `-0.0047` n `6`; index avg `0.0027` n `26`; metal avg `-0.0057` n `20`; unknown avg `0.8594` n `961`
- 1h: commodity avg `-0.0606` n `12`; crypto_alt avg `0.5319` n `234`; crypto_major avg `0.278` n `8`; equity avg `0.0069` n `141`; fx avg `-0.0132` n `6`; index avg `0.0037` n `26`; metal avg `-0.0118` n `20`; unknown avg `1.9123` n `959`
- 4h: commodity avg `0.0124` n `12`; crypto_alt avg `0.9325` n `234`; crypto_major avg `0.2049` n `8`; equity avg `0.0733` n `141`; fx avg `-0.0179` n `6`; index avg `0.0096` n `26`; metal avg `-0.0053` n `20`; unknown avg `7.5907` n `949`
- 24h: commodity avg `0.0371` n `12`; crypto_alt avg `4.1391` n `234`; crypto_major avg `0.9346` n `8`; equity avg `0.4547` n `141`; fx avg `-0.0044` n `6`; index avg `0.1439` n `26`; metal avg `0.1084` n `20`; unknown avg `-0.1881` n `820`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
