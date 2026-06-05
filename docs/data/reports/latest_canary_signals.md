# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T00:07:24.541019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `-0.0463` n `228`; crypto_major avg `-0.1454` n `8`; equity avg `-0.2698` n `74`; fx avg `-0.007` n `6`; index avg `-0.186` n `23`; metal avg `-0.1502` n `18`; unknown avg `0.9024` n `424`
- 1h: commodity avg `0.0398` n `12`; crypto_alt avg `-0.1453` n `228`; crypto_major avg `-0.3088` n `8`; equity avg `-0.528` n `74`; fx avg `-0.003` n `6`; index avg `-0.3839` n `23`; metal avg `-0.2361` n `18`; unknown avg `0.7138` n `424`
- 4h: commodity avg `0.0359` n `12`; crypto_alt avg `-1.0842` n `228`; crypto_major avg `-0.2257` n `8`; equity avg `-0.881` n `74`; fx avg `-0.0006` n `6`; index avg `-0.5435` n `23`; metal avg `-0.3897` n `18`; unknown avg `-0.7717` n `424`
- 24h: commodity avg `-0.4415` n `12`; crypto_alt avg `-6.5305` n `228`; crypto_major avg `-4.0092` n `8`; equity avg `-0.7887` n `73`; fx avg `0.0524` n `6`; index avg `-0.1327` n `23`; metal avg `0.3192` n `18`; unknown avg `-0.6274` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
