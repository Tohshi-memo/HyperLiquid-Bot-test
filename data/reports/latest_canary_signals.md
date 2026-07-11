# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T17:37:26.854258+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `0.2232` n `230`; crypto_major avg `0.1729` n `8`; equity avg `0.0406` n `92`; fx avg `0.0` n `6`; index avg `0.0038` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.0305` n `765`
- 1h: commodity avg `0.0297` n `12`; crypto_alt avg `0.2714` n `230`; crypto_major avg `0.2567` n `8`; equity avg `0.1065` n `92`; fx avg `0.0194` n `6`; index avg `0.0034` n `25`; metal avg `-0.0039` n `20`; unknown avg `0.1967` n `765`
- 4h: commodity avg `-0.018` n `12`; crypto_alt avg `0.2888` n `230`; crypto_major avg `0.4223` n `8`; equity avg `0.0966` n `92`; fx avg `-0.0031` n `6`; index avg `0.0172` n `25`; metal avg `-0.0262` n `20`; unknown avg `0.3332` n `765`
- 24h: commodity avg `0.061` n `12`; crypto_alt avg `1.0353` n `229`; crypto_major avg `0.8317` n `8`; equity avg `0.1146` n `92`; fx avg `-0.0052` n `6`; index avg `0.024` n `25`; metal avg `0.0554` n `20`; unknown avg `2.4135` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
