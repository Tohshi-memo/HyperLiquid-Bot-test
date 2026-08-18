# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T20:07:33.509597+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.008` n `12`; crypto_alt avg `-0.0137` n `230`; crypto_major avg `-0.0315` n `8`; equity avg `-0.012` n `120`; fx avg `-0.0083` n `6`; index avg `-0.0274` n `25`; metal avg `0.0087` n `20`; unknown avg `0.0136` n `789`
- 1h: commodity avg `0.0031` n `12`; crypto_alt avg `-0.1949` n `230`; crypto_major avg `-0.0694` n `8`; equity avg `-0.0154` n `120`; fx avg `-0.0125` n `6`; index avg `-0.0333` n `25`; metal avg `-0.0939` n `20`; unknown avg `-0.0278` n `789`
- 4h: commodity avg `0.0771` n `12`; crypto_alt avg `-0.5328` n `230`; crypto_major avg `-0.1955` n `8`; equity avg `-0.6337` n `120`; fx avg `-0.0015` n `6`; index avg `-0.0754` n `25`; metal avg `-0.1813` n `20`; unknown avg `0.2048` n `789`
- 24h: commodity avg `0.2748` n `12`; crypto_alt avg `-0.5574` n `230`; crypto_major avg `0.3483` n `8`; equity avg `-4.379` n `120`; fx avg `-0.0472` n `6`; index avg `-0.6953` n `25`; metal avg `-0.7663` n `20`; unknown avg `-0.2541` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
