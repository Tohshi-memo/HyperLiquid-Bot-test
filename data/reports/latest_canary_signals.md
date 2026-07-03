# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T21:37:29.584398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0248` n `12`; crypto_alt avg `-0.1092` n `229`; crypto_major avg `-0.1507` n `8`; equity avg `0.0332` n `88`; fx avg `-0.0269` n `6`; index avg `-0.008` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.0457` n `765`
- 1h: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.2333` n `229`; crypto_major avg `-0.3353` n `8`; equity avg `0.0366` n `88`; fx avg `-0.0189` n `6`; index avg `-0.0031` n `25`; metal avg `0.0172` n `20`; unknown avg `0.1078` n `765`
- 4h: commodity avg `-0.0822` n `12`; crypto_alt avg `0.5184` n `229`; crypto_major avg `0.6828` n `8`; equity avg `0.034` n `88`; fx avg `-0.0343` n `6`; index avg `-0.0564` n `25`; metal avg `-0.002` n `20`; unknown avg `0.8931` n `765`
- 24h: commodity avg `0.1053` n `12`; crypto_alt avg `3.1077` n `229`; crypto_major avg `3.2344` n `8`; equity avg `1.8576` n `88`; fx avg `-0.0999` n `6`; index avg `0.4649` n `25`; metal avg `0.5522` n `20`; unknown avg `10.7389` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
