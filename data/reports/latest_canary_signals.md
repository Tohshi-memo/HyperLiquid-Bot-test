# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T09:19:13.187714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0643` n `12`; crypto_alt avg `-0.1666` n `228`; crypto_major avg `-0.1442` n `8`; equity avg `-0.1109` n `74`; fx avg `0.0051` n `6`; index avg `-0.0114` n `23`; metal avg `0.0254` n `18`; unknown avg `0.0213` n `556`
- 1h: commodity avg `0.1127` n `12`; crypto_alt avg `-0.3127` n `228`; crypto_major avg `-0.2049` n `8`; equity avg `-0.0641` n `74`; fx avg `-0.0062` n `6`; index avg `0.0329` n `23`; metal avg `-0.3375` n `18`; unknown avg `4.0902` n `556`
- 4h: commodity avg `-0.6562` n `12`; crypto_alt avg `-0.1652` n `228`; crypto_major avg `0.3191` n `8`; equity avg `0.6587` n `74`; fx avg `0.0137` n `6`; index avg `0.3977` n `23`; metal avg `0.1217` n `18`; unknown avg `4.3067` n `530`
- 24h: commodity avg `0.8395` n `12`; crypto_alt avg `1.9688` n `228`; crypto_major avg `2.044` n `8`; equity avg `1.3216` n `74`; fx avg `0.0212` n `6`; index avg `0.3049` n `23`; metal avg `-0.2596` n `18`; unknown avg `8.1313` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
