# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T06:42:52.099299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0657` n `12`; crypto_alt avg `0.0954` n `234`; crypto_major avg `0.0861` n `8`; equity avg `-0.0519` n `141`; fx avg `0.0052` n `6`; index avg `-0.0105` n `26`; metal avg `-0.036` n `20`; unknown avg `0.5032` n `945`
- 1h: commodity avg `0.129` n `12`; crypto_alt avg `-0.0886` n `234`; crypto_major avg `-0.0024` n `8`; equity avg `-0.3772` n `141`; fx avg `0.0294` n `6`; index avg `-0.064` n `26`; metal avg `-0.0515` n `20`; unknown avg `0.5894` n `927`
- 4h: commodity avg `0.2643` n `12`; crypto_alt avg `0.937` n `234`; crypto_major avg `0.3789` n `8`; equity avg `-0.509` n `141`; fx avg `0.0306` n `6`; index avg `-0.0995` n `26`; metal avg `-0.0429` n `20`; unknown avg `1.9531` n `921`
- 24h: commodity avg `0.749` n `12`; crypto_alt avg `-4.2084` n `234`; crypto_major avg `-3.8826` n `8`; equity avg `-2.2478` n `140`; fx avg `0.0533` n `6`; index avg `-0.4648` n `26`; metal avg `-0.5776` n `20`; unknown avg `586.2453` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
