# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T23:22:28.121778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `12`; crypto_alt avg `-0.0329` n `230`; crypto_major avg `-0.0517` n `8`; equity avg `-0.1103` n `102`; fx avg `0.0257` n `6`; index avg `-0.0373` n `25`; metal avg `-0.0379` n `20`; unknown avg `2.1545` n `779`
- 1h: commodity avg `-0.0406` n `12`; crypto_alt avg `0.0147` n `230`; crypto_major avg `0.046` n `8`; equity avg `-0.0657` n `102`; fx avg `0.0091` n `6`; index avg `-0.0388` n `25`; metal avg `-0.0228` n `20`; unknown avg `-0.0889` n `779`
- 4h: commodity avg `0.0832` n `12`; crypto_alt avg `0.1195` n `230`; crypto_major avg `0.1244` n `8`; equity avg `0.9774` n `102`; fx avg `0.0633` n `6`; index avg `0.0613` n `25`; metal avg `-0.0199` n `20`; unknown avg `-0.0868` n `779`
- 24h: commodity avg `-0.0565` n `12`; crypto_alt avg `0.7998` n `230`; crypto_major avg `1.6827` n `8`; equity avg `7.5142` n `102`; fx avg `-0.3922` n `6`; index avg `0.8261` n `25`; metal avg `0.4366` n `20`; unknown avg `0.0899` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
