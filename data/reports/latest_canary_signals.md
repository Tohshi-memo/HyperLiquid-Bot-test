# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T20:37:25.510077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0274` n `12`; crypto_alt avg `0.0116` n `230`; crypto_major avg `0.0034` n `8`; equity avg `-0.0134` n `92`; fx avg `-0.0005` n `6`; index avg `-0.0016` n `25`; metal avg `0.0109` n `20`; unknown avg `-0.0247` n `765`
- 1h: commodity avg `0.0204` n `12`; crypto_alt avg `0.1771` n `230`; crypto_major avg `0.1166` n `8`; equity avg `0.0142` n `92`; fx avg `0.0004` n `6`; index avg `-0.0069` n `25`; metal avg `0.0027` n `20`; unknown avg `-0.1224` n `765`
- 4h: commodity avg `0.0562` n `12`; crypto_alt avg `0.4754` n `230`; crypto_major avg `0.3674` n `8`; equity avg `0.1951` n `92`; fx avg `0.0146` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0028` n `20`; unknown avg `0.0003` n `765`
- 24h: commodity avg `0.0411` n `12`; crypto_alt avg `1.2903` n `229`; crypto_major avg `0.9204` n `8`; equity avg `0.3941` n `92`; fx avg `0.0169` n `6`; index avg `0.0155` n `25`; metal avg `0.0113` n `20`; unknown avg `2.3898` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
