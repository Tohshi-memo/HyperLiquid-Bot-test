# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T15:37:28.761176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `0.1454` n `234`; crypto_major avg `0.0164` n `8`; equity avg `-0.0038` n `140`; fx avg `0.011` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0024` n `20`; unknown avg `0.0096` n `943`
- 1h: commodity avg `-0.0021` n `12`; crypto_alt avg `0.509` n `234`; crypto_major avg `0.2936` n `8`; equity avg `0.0701` n `140`; fx avg `0.0125` n `6`; index avg `0.0067` n `26`; metal avg `-0.0015` n `20`; unknown avg `-0.1628` n `941`
- 4h: commodity avg `0.0297` n `12`; crypto_alt avg `0.5702` n `234`; crypto_major avg `0.4533` n `8`; equity avg `0.0651` n `140`; fx avg `-0.0302` n `6`; index avg `0.0084` n `26`; metal avg `0.0033` n `20`; unknown avg `2.7193` n `935`
- 24h: commodity avg `0.4223` n `12`; crypto_alt avg `-1.6566` n `234`; crypto_major avg `-2.1042` n `8`; equity avg `-0.2488` n `140`; fx avg `-0.0483` n `6`; index avg `-0.0533` n `26`; metal avg `-0.0333` n `20`; unknown avg `236.4018` n `819`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
