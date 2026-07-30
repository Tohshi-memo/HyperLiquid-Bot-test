# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T20:07:33.376849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0014` n `12`; crypto_alt avg `0.1126` n `230`; crypto_major avg `0.0119` n `8`; equity avg `0.3988` n `102`; fx avg `-0.0036` n `6`; index avg `0.0901` n `25`; metal avg `0.0378` n `20`; unknown avg `0.0297` n `779`
- 1h: commodity avg `0.0133` n `12`; crypto_alt avg `0.2577` n `230`; crypto_major avg `0.0992` n `8`; equity avg `0.5472` n `102`; fx avg `0.0417` n `6`; index avg `0.1073` n `25`; metal avg `0.0832` n `20`; unknown avg `-0.0418` n `779`
- 4h: commodity avg `-0.0996` n `12`; crypto_alt avg `0.2236` n `230`; crypto_major avg `0.2127` n `8`; equity avg `0.8145` n `102`; fx avg `0.0126` n `6`; index avg `0.1638` n `25`; metal avg `0.1498` n `20`; unknown avg `-0.1334` n `779`
- 24h: commodity avg `-0.1569` n `12`; crypto_alt avg `1.6564` n `230`; crypto_major avg `2.3142` n `8`; equity avg `6.9014` n `102`; fx avg `-0.3926` n `6`; index avg `1.065` n `25`; metal avg `0.8293` n `20`; unknown avg `0.1856` n `738`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
