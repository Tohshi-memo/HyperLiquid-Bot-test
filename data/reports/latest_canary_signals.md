# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T23:37:24.349062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0348` n `12`; crypto_alt avg `-0.0726` n `230`; crypto_major avg `-0.0188` n `8`; equity avg `0.1082` n `102`; fx avg `-0.0056` n `6`; index avg `-0.004` n `25`; metal avg `0.0042` n `20`; unknown avg `-0.009` n `778`
- 1h: commodity avg `-0.0091` n `12`; crypto_alt avg `0.077` n `230`; crypto_major avg `0.0348` n `8`; equity avg `-0.0372` n `102`; fx avg `-0.0089` n `6`; index avg `0.025` n `25`; metal avg `0.0996` n `20`; unknown avg `-0.0315` n `778`
- 4h: commodity avg `-0.1016` n `12`; crypto_alt avg `-0.1179` n `230`; crypto_major avg `0.1025` n `8`; equity avg `-1.159` n `102`; fx avg `0.0371` n `6`; index avg `-0.213` n `25`; metal avg `0.0871` n `20`; unknown avg `0.5548` n `778`
- 24h: commodity avg `0.5226` n `12`; crypto_alt avg `-2.0368` n `230`; crypto_major avg `-0.0877` n `8`; equity avg `-3.0381` n `102`; fx avg `0.0475` n `6`; index avg `-0.5359` n `25`; metal avg `0.4626` n `20`; unknown avg `-0.629` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
