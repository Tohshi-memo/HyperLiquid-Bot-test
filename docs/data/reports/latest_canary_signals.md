# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T14:22:36.131515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `2.1485` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `2.0637` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `-0.0967` n `230`; crypto_major avg `-0.045` n `8`; equity avg `-0.2562` n `121`; fx avg `-0.0041` n `6`; index avg `-0.0754` n `25`; metal avg `-0.0085` n `20`; unknown avg `-0.0178` n `792`
- 1h: commodity avg `-0.004` n `12`; crypto_alt avg `-0.0496` n `230`; crypto_major avg `-0.0648` n `8`; equity avg `-2.2133` n `121`; fx avg `0.032` n `6`; index avg `-0.2847` n `25`; metal avg `0.039` n `20`; unknown avg `0.2001` n `792`
- 4h: commodity avg `0.0387` n `12`; crypto_alt avg `0.5525` n `230`; crypto_major avg `0.9205` n `8`; equity avg `-1.1432` n `120`; fx avg `0.0403` n `6`; index avg `-0.0747` n `25`; metal avg `0.6156` n `20`; unknown avg `0.6319` n `791`
- 24h: commodity avg `0.4071` n `12`; crypto_alt avg `0.4793` n `230`; crypto_major avg `0.952` n `8`; equity avg `-2.2451` n `120`; fx avg `-0.2064` n `6`; index avg `-0.2219` n `25`; metal avg `0.3145` n `20`; unknown avg `0.0065` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1668`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
