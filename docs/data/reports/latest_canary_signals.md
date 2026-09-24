# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T00:37:24.532561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0375` n `12`; crypto_alt avg `0.0196` n `234`; crypto_major avg `-0.0065` n `8`; equity avg `0.0447` n `141`; fx avg `0.0015` n `6`; index avg `0.0082` n `26`; metal avg `0.0427` n `20`; unknown avg `-0.1075` n `945`
- 1h: commodity avg `-0.0691` n `12`; crypto_alt avg `0.2653` n `234`; crypto_major avg `0.1987` n `8`; equity avg `-0.0575` n `141`; fx avg `0.0086` n `6`; index avg `-0.0184` n `26`; metal avg `-0.0164` n `20`; unknown avg `-0.0579` n `937`
- 4h: commodity avg `-0.2239` n `12`; crypto_alt avg `0.461` n `234`; crypto_major avg `0.6594` n `8`; equity avg `0.0228` n `141`; fx avg `-0.012` n `6`; index avg `-0.0238` n `26`; metal avg `-0.0259` n `20`; unknown avg `-0.4962` n `921`
- 24h: commodity avg `0.3491` n `12`; crypto_alt avg `-4.4876` n `234`; crypto_major avg `-3.4742` n `8`; equity avg `-1.7204` n `140`; fx avg `0.0733` n `6`; index avg `-0.3568` n `26`; metal avg `-0.8663` n `20`; unknown avg `583.13` n `821`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
