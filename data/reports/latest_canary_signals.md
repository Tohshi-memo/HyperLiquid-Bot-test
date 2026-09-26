# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T15:07:27.650835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.02` n `12`; crypto_alt avg `0.0952` n `234`; crypto_major avg `-0.0103` n `8`; equity avg `-0.0018` n `141`; fx avg `-0.0087` n `6`; index avg `0.0039` n `26`; metal avg `-0.0039` n `20`; unknown avg `0.239` n `959`
- 1h: commodity avg `-0.0156` n `12`; crypto_alt avg `0.7411` n `234`; crypto_major avg `0.2419` n `8`; equity avg `0.0945` n `141`; fx avg `-0.0122` n `6`; index avg `0.0108` n `26`; metal avg `0.0032` n `20`; unknown avg `16.3823` n `959`
- 4h: commodity avg `0.0569` n `12`; crypto_alt avg `0.4889` n `234`; crypto_major avg `0.0814` n `8`; equity avg `0.0884` n `141`; fx avg `0.0032` n `6`; index avg `0.0075` n `26`; metal avg `0.0062` n `20`; unknown avg `1.879` n `949`
- 24h: commodity avg `0.1498` n `12`; crypto_alt avg `2.7926` n `234`; crypto_major avg `-0.2577` n `8`; equity avg `0.0916` n `141`; fx avg `-0.0051` n `6`; index avg `0.0629` n `26`; metal avg `0.0645` n `20`; unknown avg `-0.4902` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
