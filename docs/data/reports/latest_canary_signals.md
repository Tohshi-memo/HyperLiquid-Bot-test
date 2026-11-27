# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T12:22:26.031396+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0422` n `13`; crypto_alt avg `0.0321` n `239`; crypto_major avg `0.0349` n `8`; equity avg `0.301` n `168`; fx avg `0.0061` n `6`; index avg `0.0417` n `27`; metal avg `-0.0101` n `20`; unknown avg `0.7939` n `1261`
- 1h: commodity avg `-0.1511` n `13`; crypto_alt avg `0.0725` n `239`; crypto_major avg `-0.2243` n `8`; equity avg `-0.4618` n `168`; fx avg `0.0283` n `6`; index avg `-0.0247` n `27`; metal avg `-0.1108` n `20`; unknown avg `244.2362` n `1249`
- 4h: commodity avg `-0.3001` n `13`; crypto_alt avg `-0.1611` n `239`; crypto_major avg `-0.3472` n `8`; equity avg `-0.553` n `168`; fx avg `0.0514` n `6`; index avg `-0.0279` n `27`; metal avg `-0.2054` n `20`; unknown avg `405.4278` n `1157`
- 24h: commodity avg `0.0281` n `13`; crypto_alt avg `1.8155` n `239`; crypto_major avg `2.9267` n `8`; equity avg `3.236` n `168`; fx avg `-0.0636` n `6`; index avg `0.2551` n `27`; metal avg `1.1237` n `20`; unknown avg `66.2137` n `1029`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
