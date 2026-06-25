# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T11:22:34.107734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5814` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3707` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0409` n `12`; crypto_alt avg `-0.0448` n `228`; crypto_major avg `0.0831` n `8`; equity avg `-0.1213` n `86`; fx avg `0.0009` n `6`; index avg `-0.0149` n `23`; metal avg `-0.0443` n `20`; unknown avg `0.0452` n `765`
- 1h: commodity avg `-0.0122` n `12`; crypto_alt avg `-0.492` n `228`; crypto_major avg `-0.7761` n `8`; equity avg `-0.1462` n `86`; fx avg `-0.0153` n `6`; index avg `0.0271` n `23`; metal avg `-0.0385` n `20`; unknown avg `-0.0887` n `765`
- 4h: commodity avg `-0.0222` n `12`; crypto_alt avg `-0.9228` n `228`; crypto_major avg `-1.3655` n `8`; equity avg `-0.0896` n `86`; fx avg `-0.0114` n `6`; index avg `0.0052` n `23`; metal avg `0.2159` n `20`; unknown avg `-0.0972` n `757`
- 24h: commodity avg `-0.2873` n `12`; crypto_alt avg `-1.1211` n `228`; crypto_major avg `-1.0823` n `8`; equity avg `0.2889` n `86`; fx avg `-0.0197` n `6`; index avg `0.5487` n `23`; metal avg `-0.8443` n `20`; unknown avg `-0.6098` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
