# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T10:22:31.059959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6296` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0998` n `12`; crypto_alt avg `-0.0271` n `234`; crypto_major avg `-0.0662` n `8`; equity avg `0.0684` n `141`; fx avg `-0.0117` n `6`; index avg `0.0115` n `26`; metal avg `-0.0256` n `20`; unknown avg `0.1155` n `945`
- 1h: commodity avg `-0.0621` n `12`; crypto_alt avg `-0.2751` n `234`; crypto_major avg `-0.4438` n `8`; equity avg `0.0884` n `141`; fx avg `-0.0167` n `6`; index avg `-0.0114` n `26`; metal avg `-0.1034` n `20`; unknown avg `0.3732` n `943`
- 4h: commodity avg `0.1804` n `12`; crypto_alt avg `-1.8693` n `234`; crypto_major avg `-1.7385` n `8`; equity avg `-0.7075` n `141`; fx avg `0.0108` n `6`; index avg `-0.1089` n `26`; metal avg `-0.249` n `20`; unknown avg `2.082` n `937`
- 24h: commodity avg `0.7303` n `12`; crypto_alt avg `-5.1551` n `234`; crypto_major avg `-4.2164` n `8`; equity avg `-2.6156` n `141`; fx avg `0.0215` n `6`; index avg `-0.4997` n `26`; metal avg `-0.5681` n `20`; unknown avg `586.8713` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
