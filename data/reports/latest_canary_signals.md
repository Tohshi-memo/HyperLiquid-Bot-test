# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T12:37:23.500707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0748` n `12`; crypto_alt avg `-0.4825` n `228`; crypto_major avg `-0.4025` n `8`; equity avg `-0.3798` n `74`; fx avg `-0.0535` n `6`; index avg `-0.217` n `23`; metal avg `-0.6919` n `18`; unknown avg `0.7572` n `424`
- 1h: commodity avg `0.0291` n `12`; crypto_alt avg `-0.7054` n `228`; crypto_major avg `-0.572` n `8`; equity avg `-0.5994` n `74`; fx avg `-0.0446` n `6`; index avg `-0.2701` n `23`; metal avg `-0.2387` n `18`; unknown avg `3.2964` n `424`
- 4h: commodity avg `0.2024` n `12`; crypto_alt avg `-0.378` n `228`; crypto_major avg `-0.3438` n `8`; equity avg `-0.4478` n `74`; fx avg `0.0025` n `6`; index avg `-0.2225` n `23`; metal avg `0.0491` n `18`; unknown avg `2.3598` n `424`
- 24h: commodity avg `-0.1359` n `12`; crypto_alt avg `-6.5191` n `228`; crypto_major avg `-4.9134` n `8`; equity avg `-1.2903` n `74`; fx avg `0.0744` n `6`; index avg `-0.225` n `23`; metal avg `-1.2833` n `18`; unknown avg `0.6981` n `404`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
