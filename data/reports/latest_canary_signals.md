# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T10:52:28.943732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `-0.0464` n `230`; crypto_major avg `-0.1283` n `8`; equity avg `0.0007` n `121`; fx avg `-0.0137` n `6`; index avg `-0.0037` n `25`; metal avg `0.0122` n `20`; unknown avg `0.2511` n `795`
- 1h: commodity avg `0.0222` n `12`; crypto_alt avg `0.566` n `230`; crypto_major avg `0.2466` n `8`; equity avg `0.0452` n `121`; fx avg `-0.0151` n `6`; index avg `0.0088` n `25`; metal avg `0.0257` n `20`; unknown avg `0.4479` n `794`
- 4h: commodity avg `-0.0114` n `12`; crypto_alt avg `2.5507` n `230`; crypto_major avg `1.3912` n `8`; equity avg `0.2653` n `121`; fx avg `0.0061` n `6`; index avg `0.0373` n `25`; metal avg `0.0102` n `20`; unknown avg `0.7697` n `794`
- 24h: commodity avg `0.0059` n `12`; crypto_alt avg `-0.0261` n `230`; crypto_major avg `0.7405` n `8`; equity avg `0.3422` n `121`; fx avg `0.0308` n `6`; index avg `0.0432` n `25`; metal avg `0.0503` n `20`; unknown avg `3.1602` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
