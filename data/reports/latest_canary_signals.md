# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T20:51:31.076993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0224` n `12`; crypto_alt avg `0.0225` n `230`; crypto_major avg `0.0579` n `8`; equity avg `0.0234` n `102`; fx avg `0.0078` n `6`; index avg `-0.017` n `25`; metal avg `-0.0247` n `20`; unknown avg `-0.0797` n `779`
- 1h: commodity avg `0.0517` n `12`; crypto_alt avg `-0.0473` n `230`; crypto_major avg `-0.1964` n `8`; equity avg `0.4461` n `102`; fx avg `0.0116` n `6`; index avg `0.0402` n `25`; metal avg `-0.0518` n `20`; unknown avg `0.0224` n `779`
- 4h: commodity avg `-0.0294` n `12`; crypto_alt avg `0.1665` n `230`; crypto_major avg `0.0307` n `8`; equity avg `1.0691` n `102`; fx avg `-0.0173` n `6`; index avg `0.1698` n `25`; metal avg `0.096` n `20`; unknown avg `-0.1686` n `779`
- 24h: commodity avg `-0.1096` n `12`; crypto_alt avg `1.856` n `230`; crypto_major avg `2.1044` n `8`; equity avg `7.4783` n `102`; fx avg `-0.3763` n `6`; index avg `0.9684` n `25`; metal avg `0.6565` n `20`; unknown avg `0.1882` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
