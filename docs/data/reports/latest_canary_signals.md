# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T21:52:36.186989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0373` n `12`; crypto_alt avg `-0.3395` n `228`; crypto_major avg `-0.3093` n `8`; equity avg `0.0094` n `74`; fx avg `0.0109` n `6`; index avg `0.0501` n `23`; metal avg `-0.011` n `18`; unknown avg `0.0285` n `643`
- 1h: commodity avg `0.0019` n `12`; crypto_alt avg `0.0036` n `228`; crypto_major avg `-0.0695` n `8`; equity avg `0.0772` n `74`; fx avg `-0.0249` n `6`; index avg `0.0096` n `23`; metal avg `-0.0572` n `18`; unknown avg `-0.3664` n `643`
- 4h: commodity avg `-0.1349` n `12`; crypto_alt avg `-0.6201` n `228`; crypto_major avg `-0.9027` n `8`; equity avg `-0.4031` n `74`; fx avg `-0.0246` n `6`; index avg `-0.0456` n `23`; metal avg `0.0442` n `18`; unknown avg `0.1983` n `643`
- 24h: commodity avg `-0.4279` n `12`; crypto_alt avg `-0.7031` n `228`; crypto_major avg `0.0708` n `8`; equity avg `-0.2968` n `74`; fx avg `-0.0172` n `6`; index avg `0.5038` n `23`; metal avg `0.5237` n `18`; unknown avg `41.1027` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
