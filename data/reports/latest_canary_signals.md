# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T06:07:31.991508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1176` n `12`; crypto_alt avg `0.2861` n `228`; crypto_major avg `0.2408` n `8`; equity avg `0.0204` n `74`; fx avg `0.0019` n `6`; index avg `-0.0542` n `23`; metal avg `0.0045` n `18`; unknown avg `0.0695` n `627`
- 1h: commodity avg `-0.1518` n `12`; crypto_alt avg `0.0421` n `228`; crypto_major avg `0.1501` n `8`; equity avg `-0.0667` n `74`; fx avg `0.0022` n `6`; index avg `0.0378` n `23`; metal avg `0.0093` n `18`; unknown avg `-0.1363` n `627`
- 4h: commodity avg `-0.2336` n `12`; crypto_alt avg `-0.6257` n `228`; crypto_major avg `-0.6969` n `8`; equity avg `-0.4108` n `74`; fx avg `0.0309` n `6`; index avg `-0.0126` n `23`; metal avg `-0.075` n `18`; unknown avg `-0.5205` n `619`
- 24h: commodity avg `-0.6798` n `12`; crypto_alt avg `0.3195` n `228`; crypto_major avg `-0.1771` n `8`; equity avg `-0.4349` n `74`; fx avg `0.0391` n `6`; index avg `0.8818` n `23`; metal avg `0.6696` n `18`; unknown avg `36.3569` n `507`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
