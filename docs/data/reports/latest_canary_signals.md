# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T21:07:34.690577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.029` n `12`; crypto_alt avg `-0.0381` n `230`; crypto_major avg `-0.0437` n `8`; equity avg `0.0171` n `113`; fx avg `-0.0069` n `6`; index avg `-0.0018` n `25`; metal avg `0.0099` n `20`; unknown avg `-0.0252` n `786`
- 1h: commodity avg `-0.0256` n `12`; crypto_alt avg `-0.0973` n `230`; crypto_major avg `0.0456` n `8`; equity avg `-0.2581` n `113`; fx avg `-0.0096` n `6`; index avg `-0.0281` n `25`; metal avg `-0.0212` n `20`; unknown avg `-0.1127` n `786`
- 4h: commodity avg `-0.0147` n `12`; crypto_alt avg `-0.3921` n `230`; crypto_major avg `-0.1625` n `8`; equity avg `-0.1232` n `113`; fx avg `-0.0047` n `6`; index avg `-0.0079` n `25`; metal avg `-0.0226` n `20`; unknown avg `-0.0392` n `786`
- 24h: commodity avg `0.057` n `12`; crypto_alt avg `-0.8515` n `230`; crypto_major avg `-0.0428` n `8`; equity avg `2.7689` n `113`; fx avg `0.0285` n `6`; index avg `0.3687` n `25`; metal avg `0.1673` n `20`; unknown avg `0.0299` n `769`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2334`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2024`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2015`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1956`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
