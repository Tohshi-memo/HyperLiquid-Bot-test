# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T07:07:30.509347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0218` n `12`; crypto_alt avg `-0.1146` n `234`; crypto_major avg `-0.0358` n `8`; equity avg `0.0437` n `141`; fx avg `0.0221` n `6`; index avg `0.0018` n `26`; metal avg `0.0671` n `20`; unknown avg `2.2882` n `943`
- 1h: commodity avg `0.0273` n `12`; crypto_alt avg `-0.0289` n `234`; crypto_major avg `-0.0534` n `8`; equity avg `-0.1138` n `141`; fx avg `0.0458` n `6`; index avg `-0.0224` n `26`; metal avg `0.0129` n `20`; unknown avg `3.0334` n `943`
- 4h: commodity avg `0.2305` n `12`; crypto_alt avg `0.2965` n `234`; crypto_major avg `-0.0904` n `8`; equity avg `-0.5112` n `141`; fx avg `0.0335` n `6`; index avg `-0.0884` n `26`; metal avg `0.0219` n `20`; unknown avg `2.797` n `921`
- 24h: commodity avg `0.693` n `12`; crypto_alt avg `-4.0955` n `234`; crypto_major avg `-3.8404` n `8`; equity avg `-2.1017` n `140`; fx avg `0.0024` n `6`; index avg `-0.4404` n `26`; metal avg `-0.465` n `20`; unknown avg `589.3721` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.162`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
