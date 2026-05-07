# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T14:22:22.212552+00:00`
- Correlation status: `ready`
- Asset price records: `557`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `12`; crypto_alt avg `0.0568` n `228`; crypto_major avg `0.031` n `8`; equity avg `0.4917` n `65`; fx avg `-0.0037` n `5`; index avg `0.1556` n `23`; metal avg `0.1551` n `18`; unknown avg `0.0846` n `365`
- 1h: commodity avg `-0.2655` n `12`; crypto_alt avg `-0.846` n `228`; crypto_major avg `-0.8696` n `8`; equity avg `-0.0795` n `65`; fx avg `-0.0037` n `5`; index avg `-0.2673` n `23`; metal avg `0.031` n `18`; unknown avg `-0.2164` n `365`
- 4h: commodity avg `-0.9641` n `12`; crypto_alt avg `0.0395` n `228`; crypto_major avg `-0.6977` n `8`; equity avg `-0.0972` n `65`; fx avg `-0.0319` n `5`; index avg `-0.3097` n `23`; metal avg `0.2924` n `18`; unknown avg `-0.0284` n `365`
- 24h: commodity avg `-1.5554` n `12`; crypto_alt avg `1.4905` n `228`; crypto_major avg `-1.3359` n `8`; equity avg `1.9027` n `65`; fx avg `0.1124` n `5`; index avg `0.6672` n `23`; metal avg `1.6763` n `18`; unknown avg `0.2796` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1359`, n `553`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1248`, n `553`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0916`, n `553`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0913`, n `553`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0815`, n `549`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0797`, n `549`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0785`, n `553`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0776`, n `549`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0741`, n `549`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0726`, n `553`, weak_sample_signal
