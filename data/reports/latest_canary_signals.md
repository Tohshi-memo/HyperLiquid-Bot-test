# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T05:37:24.073640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `12`; crypto_alt avg `0.102` n `230`; crypto_major avg `0.0381` n `8`; equity avg `0.0395` n `120`; fx avg `-0.025` n `6`; index avg `0.0062` n `25`; metal avg `0.0096` n `20`; unknown avg `-0.0518` n `789`
- 1h: commodity avg `-0.0002` n `12`; crypto_alt avg `0.1343` n `230`; crypto_major avg `-0.0244` n `8`; equity avg `-0.1348` n `120`; fx avg `-0.0528` n `6`; index avg `-0.0209` n `25`; metal avg `-0.0635` n `20`; unknown avg `-0.0565` n `789`
- 4h: commodity avg `-0.0173` n `12`; crypto_alt avg `-0.0857` n `230`; crypto_major avg `-0.0686` n `8`; equity avg `-0.7702` n `120`; fx avg `-0.1276` n `6`; index avg `-0.1163` n `25`; metal avg `-0.1082` n `20`; unknown avg `-0.1773` n `789`
- 24h: commodity avg `0.3418` n `12`; crypto_alt avg `0.8578` n `230`; crypto_major avg `0.4454` n `8`; equity avg `-3.1905` n `120`; fx avg `-0.1923` n `6`; index avg `-0.4942` n `25`; metal avg `-0.5944` n `20`; unknown avg `-0.2102` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
