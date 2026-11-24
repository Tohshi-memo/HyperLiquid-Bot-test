# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T10:37:28.396738+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `13`; crypto_alt avg `-0.2797` n `239`; crypto_major avg `-0.2577` n `8`; equity avg `-0.3306` n `166`; fx avg `0.0027` n `6`; index avg `-0.0437` n `27`; metal avg `0.0448` n `20`; unknown avg `-0.0737` n `1266`
- 1h: commodity avg `0.0196` n `13`; crypto_alt avg `-0.4056` n `239`; crypto_major avg `-0.3955` n `8`; equity avg `-0.5664` n `166`; fx avg `0.0372` n `6`; index avg `-0.0899` n `27`; metal avg `0.0266` n `20`; unknown avg `-0.0166` n `1218`
- 4h: commodity avg `0.3116` n `13`; crypto_alt avg `-1.7826` n `239`; crypto_major avg `-1.2281` n `8`; equity avg `-2.1468` n `166`; fx avg `0.072` n `6`; index avg `-0.2626` n `27`; metal avg `-0.0615` n `20`; unknown avg `0.2194` n `1200`
- 24h: commodity avg `-0.5448` n `13`; crypto_alt avg `-1.2095` n `239`; crypto_major avg `-1.519` n `8`; equity avg `1.1924` n `166`; fx avg `-0.0938` n `6`; index avg `0.296` n `27`; metal avg `-0.357` n `20`; unknown avg `0.2427` n `1134`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
