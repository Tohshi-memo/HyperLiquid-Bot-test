# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T05:07:28.707033+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.02` n `12`; crypto_alt avg `-0.1567` n `234`; crypto_major avg `-0.0649` n `8`; equity avg `0.0532` n `141`; fx avg `0.0006` n `6`; index avg `0.0094` n `26`; metal avg `-0.0001` n `20`; unknown avg `-0.0803` n `959`
- 1h: commodity avg `0.0045` n `12`; crypto_alt avg `-0.2096` n `234`; crypto_major avg `-0.1427` n `8`; equity avg `0.0575` n `141`; fx avg `0.0018` n `6`; index avg `0.0015` n `26`; metal avg `-0.0026` n `20`; unknown avg `-0.4998` n `959`
- 4h: commodity avg `-0.0833` n `12`; crypto_alt avg `-0.0381` n `234`; crypto_major avg `-0.3319` n `8`; equity avg `0.1055` n `141`; fx avg `0.0069` n `6`; index avg `0.0248` n `26`; metal avg `-0.0043` n `20`; unknown avg `13.0384` n `952`
- 24h: commodity avg `0.0238` n `12`; crypto_alt avg `3.2001` n `234`; crypto_major avg `1.1041` n `8`; equity avg `-0.3429` n `141`; fx avg `-0.1162` n `6`; index avg `0.131` n `26`; metal avg `0.2922` n `20`; unknown avg `1127.5328` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
