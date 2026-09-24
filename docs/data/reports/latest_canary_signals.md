# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T12:37:26.139647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0539` n `12`; crypto_alt avg `-0.3742` n `234`; crypto_major avg `-0.3167` n `8`; equity avg `-0.4056` n `141`; fx avg `-0.0003` n `6`; index avg `-0.0421` n `26`; metal avg `-0.0837` n `20`; unknown avg `-0.1069` n `945`
- 1h: commodity avg `-0.0494` n `12`; crypto_alt avg `-0.0019` n `234`; crypto_major avg `0.032` n `8`; equity avg `-0.3037` n `141`; fx avg `-0.0253` n `6`; index avg `-0.0115` n `26`; metal avg `-0.0024` n `20`; unknown avg `0.3437` n `937`
- 4h: commodity avg `-0.2329` n `12`; crypto_alt avg `-0.7596` n `234`; crypto_major avg `-0.8342` n `8`; equity avg `-0.0898` n `141`; fx avg `-0.0299` n `6`; index avg `0.0029` n `26`; metal avg `-0.0255` n `20`; unknown avg `0.8162` n `937`
- 24h: commodity avg `0.4294` n `12`; crypto_alt avg `-4.4336` n `234`; crypto_major avg `-3.5326` n `8`; equity avg `-2.3216` n `141`; fx avg `-0.0146` n `6`; index avg `-0.4195` n `26`; metal avg `-0.3073` n `20`; unknown avg `588.4568` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
