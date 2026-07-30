# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T20:22:31.190900+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.066` n `12`; crypto_alt avg `-0.0977` n `230`; crypto_major avg `-0.0796` n `8`; equity avg `0.0548` n `102`; fx avg `-0.004` n `6`; index avg `-0.0083` n `25`; metal avg `-0.0183` n `20`; unknown avg `0.0002` n `779`
- 1h: commodity avg `0.0848` n `12`; crypto_alt avg `0.1678` n `230`; crypto_major avg `-0.0185` n `8`; equity avg `0.4977` n `102`; fx avg `0.0284` n `6`; index avg `0.0727` n `25`; metal avg `0.0181` n `20`; unknown avg `-0.0226` n `779`
- 4h: commodity avg `0.0653` n `12`; crypto_alt avg `0.2056` n `230`; crypto_major avg `0.2715` n `8`; equity avg `0.855` n `102`; fx avg `-0.0011` n `6`; index avg `0.139` n `25`; metal avg `0.1041` n `20`; unknown avg `-0.1635` n `779`
- 24h: commodity avg `-0.1234` n `12`; crypto_alt avg `1.5242` n `230`; crypto_major avg `2.108` n `8`; equity avg `7.2179` n `102`; fx avg `-0.389` n `6`; index avg `1.0357` n `25`; metal avg `0.8435` n `20`; unknown avg `0.1581` n `738`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
