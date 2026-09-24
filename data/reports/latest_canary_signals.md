# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T21:37:28.822651+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0301` n `12`; crypto_alt avg `0.1234` n `234`; crypto_major avg `0.0527` n `8`; equity avg `0.0221` n `141`; fx avg `-0.0063` n `6`; index avg `0.0021` n `26`; metal avg `-0.0103` n `20`; unknown avg `3.1999` n `946`
- 1h: commodity avg `-0.1073` n `12`; crypto_alt avg `0.6299` n `234`; crypto_major avg `0.2279` n `8`; equity avg `0.1427` n `141`; fx avg `-0.0181` n `6`; index avg `0.0225` n `26`; metal avg `0.0204` n `20`; unknown avg `5.9306` n `942`
- 4h: commodity avg `-0.2109` n `12`; crypto_alt avg `0.5649` n `234`; crypto_major avg `0.2291` n `8`; equity avg `-0.0014` n `141`; fx avg `-0.0311` n `6`; index avg `-0.0191` n `26`; metal avg `0.0355` n `20`; unknown avg `7.7979` n `869`
- 24h: commodity avg `0.7183` n `12`; crypto_alt avg `4.1282` n `234`; crypto_major avg `1.4423` n `8`; equity avg `-0.2505` n `141`; fx avg `0.0243` n `6`; index avg `-0.1109` n `26`; metal avg `-0.1331` n `20`; unknown avg `19.4619` n `855`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
