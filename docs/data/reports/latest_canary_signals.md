# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T20:22:31.814585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0149` n `13`; crypto_alt avg `-0.7189` n `238`; crypto_major avg `-0.5022` n `8`; equity avg `-0.7941` n `155`; fx avg `-0.0075` n `6`; index avg `-0.1021` n `27`; metal avg `-0.0607` n `20`; unknown avg `1.3163` n `1230`
- 1h: commodity avg `-0.2758` n `13`; crypto_alt avg `0.3547` n `238`; crypto_major avg `0.1913` n `8`; equity avg `-0.3154` n `155`; fx avg `-0.0036` n `6`; index avg `0.0099` n `27`; metal avg `0.1016` n `20`; unknown avg `13.456` n `1192`
- 4h: commodity avg `-0.5396` n `13`; crypto_alt avg `1.2699` n `238`; crypto_major avg `1.0184` n `8`; equity avg `0.1597` n `155`; fx avg `-0.018` n `6`; index avg `0.0163` n `27`; metal avg `0.1729` n `20`; unknown avg `6.3693` n `1194`
- 24h: commodity avg `0.047` n `13`; crypto_alt avg `0.9241` n `238`; crypto_major avg `0.7233` n `8`; equity avg `1.3689` n `154`; fx avg `0.2442` n `6`; index avg `0.2743` n `27`; metal avg `-0.0241` n `20`; unknown avg `7.4045` n `1054`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
