# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T02:53:05.853382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0731` n `12`; crypto_alt avg `0.2508` n `232`; crypto_major avg `0.1588` n `8`; equity avg `0.0096` n `133`; fx avg `0.0003` n `6`; index avg `-0.0018` n `26`; metal avg `-0.0159` n `20`; unknown avg `-0.0332` n `792`
- 1h: commodity avg `-0.0536` n `12`; crypto_alt avg `0.5986` n `232`; crypto_major avg `0.7499` n `8`; equity avg `0.0694` n `133`; fx avg `-0.0408` n `6`; index avg `0.0093` n `26`; metal avg `0.0078` n `20`; unknown avg `0.7006` n `790`
- 4h: commodity avg `0.0399` n `12`; crypto_alt avg `1.3992` n `232`; crypto_major avg `1.3215` n `8`; equity avg `0.1782` n `133`; fx avg `-0.0825` n `6`; index avg `-0.0152` n `26`; metal avg `0.1507` n `20`; unknown avg `0.9138` n `790`
- 24h: commodity avg `0.1561` n `12`; crypto_alt avg `0.7855` n `232`; crypto_major avg `0.8793` n `8`; equity avg `1.3563` n `133`; fx avg `-0.3931` n `6`; index avg `0.1287` n `26`; metal avg `0.7712` n `20`; unknown avg `-0.3648` n `751`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
