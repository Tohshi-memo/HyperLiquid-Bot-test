# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T19:37:27.209833+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0287` n `12`; crypto_alt avg `0.6416` n `228`; crypto_major avg `0.3985` n `8`; equity avg `0.6535` n `74`; fx avg `0.0062` n `6`; index avg `0.3034` n `23`; metal avg `0.1438` n `18`; unknown avg `0.304` n `425`
- 1h: commodity avg `-0.2321` n `12`; crypto_alt avg `-0.8069` n `228`; crypto_major avg `-0.4358` n `8`; equity avg `0.3185` n `74`; fx avg `-0.0164` n `6`; index avg `-0.4884` n `23`; metal avg `-0.0513` n `18`; unknown avg `-0.148` n `424`
- 4h: commodity avg `-0.3343` n `12`; crypto_alt avg `-1.4688` n `228`; crypto_major avg `-1.3663` n `8`; equity avg `-1.8225` n `74`; fx avg `-0.0764` n `6`; index avg `-1.8473` n `23`; metal avg `-0.6089` n `18`; unknown avg `-0.7966` n `424`
- 24h: commodity avg `-1.6395` n `12`; crypto_alt avg `-10.3861` n `228`; crypto_major avg `-8.4636` n `8`; equity avg `-6.7614` n `74`; fx avg `-0.0556` n `6`; index avg `-4.3588` n `23`; metal avg `-4.5868` n `18`; unknown avg `-2.5115` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
