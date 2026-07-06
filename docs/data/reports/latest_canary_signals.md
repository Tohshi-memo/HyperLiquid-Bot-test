# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T15:37:29.529964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0883` n `12`; crypto_alt avg `0.0743` n `229`; crypto_major avg `-0.0019` n `8`; equity avg `0.027` n `88`; fx avg `-0.0018` n `6`; index avg `0.0482` n `25`; metal avg `0.0408` n `20`; unknown avg `-0.091` n `765`
- 1h: commodity avg `-0.007` n `12`; crypto_alt avg `0.344` n `229`; crypto_major avg `0.4877` n `8`; equity avg `-0.1192` n `88`; fx avg `-0.0057` n `6`; index avg `0.0061` n `25`; metal avg `0.0128` n `20`; unknown avg `-0.0227` n `765`
- 4h: commodity avg `0.2148` n `12`; crypto_alt avg `-0.0472` n `229`; crypto_major avg `-0.7707` n `8`; equity avg `0.4752` n `88`; fx avg `0.0248` n `6`; index avg `0.1171` n `25`; metal avg `-0.1662` n `20`; unknown avg `-0.3441` n `765`
- 24h: commodity avg `0.067` n `12`; crypto_alt avg `-0.2216` n `229`; crypto_major avg `-0.6924` n `8`; equity avg `-0.2771` n `88`; fx avg `0.1888` n `6`; index avg `0.0858` n `25`; metal avg `-0.3188` n `20`; unknown avg `0.419` n `679`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
