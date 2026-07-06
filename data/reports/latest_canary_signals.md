# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T00:37:25.636645+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0417` n `12`; crypto_alt avg `-0.0747` n `229`; crypto_major avg `0.0554` n `8`; equity avg `-0.2041` n `88`; fx avg `-0.0152` n `6`; index avg `-0.0667` n `25`; metal avg `0.0364` n `20`; unknown avg `3.7876` n `765`
- 1h: commodity avg `-0.0397` n `12`; crypto_alt avg `-0.3833` n `229`; crypto_major avg `-0.2313` n `8`; equity avg `-0.3373` n `88`; fx avg `0.0281` n `6`; index avg `0.0385` n `25`; metal avg `-0.1252` n `20`; unknown avg `-0.2139` n `765`
- 4h: commodity avg `-0.1743` n `12`; crypto_alt avg `0.2729` n `229`; crypto_major avg `0.7833` n `8`; equity avg `-0.2573` n `88`; fx avg `0.1227` n `6`; index avg `0.0573` n `25`; metal avg `0.0516` n `20`; unknown avg `0.7165` n `765`
- 24h: commodity avg `-0.2124` n `12`; crypto_alt avg `0.0372` n `229`; crypto_major avg `1.0665` n `8`; equity avg `0.0731` n `88`; fx avg `0.0524` n `6`; index avg `0.1364` n `25`; metal avg `0.0782` n `20`; unknown avg `1.3704` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0491`, n `668`, weak_sample_signal
