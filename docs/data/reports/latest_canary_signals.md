# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T12:37:26.850985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0391` n `12`; crypto_alt avg `-0.0509` n `230`; crypto_major avg `-0.3174` n `8`; equity avg `-0.2078` n `94`; fx avg `-0.0207` n `6`; index avg `-0.0511` n `25`; metal avg `-0.0777` n `20`; unknown avg `-0.0684` n `768`
- 1h: commodity avg `0.3224` n `12`; crypto_alt avg `-0.0407` n `230`; crypto_major avg `-0.3349` n `8`; equity avg `-0.3633` n `94`; fx avg `0.0088` n `6`; index avg `-0.1145` n `25`; metal avg `-0.1835` n `20`; unknown avg `0.1175` n `768`
- 4h: commodity avg `0.3486` n `12`; crypto_alt avg `-0.1205` n `230`; crypto_major avg `-0.596` n `8`; equity avg `-0.735` n `94`; fx avg `-0.0212` n `6`; index avg `-0.2097` n `25`; metal avg `-0.2369` n `20`; unknown avg `-0.0099` n `762`
- 24h: commodity avg `0.3114` n `12`; crypto_alt avg `-1.1458` n `230`; crypto_major avg `-1.458` n `8`; equity avg `-3.502` n `93`; fx avg `0.0303` n `6`; index avg `-0.6522` n `25`; metal avg `-0.382` n `20`; unknown avg `0.0612` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0774`, n `668`, weak_sample_signal
