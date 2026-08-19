# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T12:22:27.569239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0188` n `12`; crypto_alt avg `0.0821` n `230`; crypto_major avg `0.0209` n `8`; equity avg `0.1016` n `120`; fx avg `-0.0086` n `6`; index avg `0.0175` n `25`; metal avg `0.0462` n `20`; unknown avg `-0.0125` n `792`
- 1h: commodity avg `0.0638` n `12`; crypto_alt avg `0.0649` n `230`; crypto_major avg `0.0311` n `8`; equity avg `-0.1327` n `120`; fx avg `-0.0227` n `6`; index avg `0.0136` n `25`; metal avg `0.0465` n `20`; unknown avg `-0.0174` n `792`
- 4h: commodity avg `0.1521` n `12`; crypto_alt avg `0.2587` n `230`; crypto_major avg `0.3196` n `8`; equity avg `-0.6309` n `120`; fx avg `-0.0617` n `6`; index avg `-0.0303` n `25`; metal avg `0.1351` n `20`; unknown avg `0.07` n `789`
- 24h: commodity avg `0.3751` n `12`; crypto_alt avg `0.3867` n `230`; crypto_major avg `0.3469` n `8`; equity avg `-1.9696` n `120`; fx avg `-0.2235` n `6`; index avg `-0.2163` n `25`; metal avg `-0.397` n `20`; unknown avg `-0.0728` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1647`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1473`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
