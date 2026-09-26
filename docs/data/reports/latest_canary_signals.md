# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T21:07:30.812753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0381` n `12`; crypto_alt avg `0.4821` n `234`; crypto_major avg `0.2616` n `8`; equity avg `0.0421` n `141`; fx avg `-0.007` n `6`; index avg `0.0003` n `26`; metal avg `0.0017` n `20`; unknown avg `15.6853` n `959`
- 1h: commodity avg `0.0169` n `12`; crypto_alt avg `-0.6186` n `234`; crypto_major avg `-0.2185` n `8`; equity avg `-0.0448` n `141`; fx avg `-0.0149` n `6`; index avg `-0.0097` n `26`; metal avg `0.0` n `20`; unknown avg `7.5902` n `959`
- 4h: commodity avg `0.0576` n `12`; crypto_alt avg `-1.6338` n `234`; crypto_major avg `-0.6983` n `8`; equity avg `-0.0845` n `141`; fx avg `-0.0131` n `6`; index avg `-0.029` n `26`; metal avg `0.0005` n `20`; unknown avg `19.6395` n `953`
- 24h: commodity avg `0.3239` n `12`; crypto_alt avg `0.9263` n `234`; crypto_major avg `-0.443` n `8`; equity avg `0.005` n `141`; fx avg `0.0115` n `6`; index avg `-0.0449` n `26`; metal avg `-0.0165` n `20`; unknown avg `4.5981` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
