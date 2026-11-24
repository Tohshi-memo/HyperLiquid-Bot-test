# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T23:37:35.807297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `13`; crypto_alt avg `-0.0989` n `239`; crypto_major avg `-0.2582` n `8`; equity avg `-0.2109` n `168`; fx avg `0.0111` n `6`; index avg `-0.0079` n `27`; metal avg `-0.0215` n `20`; unknown avg `88.7701` n `1265`
- 1h: commodity avg `0.0421` n `13`; crypto_alt avg `-0.313` n `239`; crypto_major avg `-0.2878` n `8`; equity avg `-0.646` n `168`; fx avg `0.0072` n `6`; index avg `-0.032` n `27`; metal avg `-0.0077` n `20`; unknown avg `-0.1012` n `1205`
- 4h: commodity avg `-0.0122` n `13`; crypto_alt avg `-0.1806` n `239`; crypto_major avg `0.2231` n `8`; equity avg `-0.0975` n `168`; fx avg `-0.0254` n `6`; index avg `-0.0203` n `27`; metal avg `0.0089` n `20`; unknown avg `1.5422` n `1161`
- 24h: commodity avg `0.6148` n `13`; crypto_alt avg `-2.8538` n `239`; crypto_major avg `-2.418` n `8`; equity avg `-4.0985` n `167`; fx avg `0.2247` n `6`; index avg `-0.2364` n `27`; metal avg `-1.0249` n `20`; unknown avg `460.2212` n `1055`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
