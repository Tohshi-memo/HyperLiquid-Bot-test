# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T05:52:24.769978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0363` n `12`; crypto_alt avg `0.0042` n `230`; crypto_major avg `-0.0163` n `8`; equity avg `0.2394` n `102`; fx avg `-0.0032` n `6`; index avg `0.0274` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.0041` n `779`
- 1h: commodity avg `0.2254` n `12`; crypto_alt avg `0.0771` n `230`; crypto_major avg `0.0231` n `8`; equity avg `0.3519` n `102`; fx avg `-0.0156` n `6`; index avg `-0.0086` n `25`; metal avg `-0.0581` n `20`; unknown avg `-0.1585` n `779`
- 4h: commodity avg `0.2655` n `12`; crypto_alt avg `-0.3223` n `230`; crypto_major avg `-0.5035` n `8`; equity avg `-1.5298` n `102`; fx avg `-0.1128` n `6`; index avg `-0.3511` n `25`; metal avg `-0.4356` n `20`; unknown avg `0.1484` n `779`
- 24h: commodity avg `0.8217` n `12`; crypto_alt avg `-0.3654` n `230`; crypto_major avg `-0.4903` n `8`; equity avg `-2.4125` n `102`; fx avg `0.0268` n `6`; index avg `-0.1588` n `25`; metal avg `-0.0863` n `20`; unknown avg `-0.569` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
