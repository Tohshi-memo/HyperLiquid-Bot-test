# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T23:48:16.784839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0246` n `12`; crypto_alt avg `0.1046` n `230`; crypto_major avg `0.1284` n `8`; equity avg `0.1842` n `102`; fx avg `-0.0125` n `6`; index avg `0.0622` n `25`; metal avg `0.0008` n `20`; unknown avg `0.0308` n `778`
- 1h: commodity avg `-0.0375` n `12`; crypto_alt avg `0.2319` n `230`; crypto_major avg `0.2155` n `8`; equity avg `0.3273` n `102`; fx avg `-0.0219` n `6`; index avg `0.0961` n `25`; metal avg `0.074` n `20`; unknown avg `0.0796` n `778`
- 4h: commodity avg `-0.1168` n `12`; crypto_alt avg `0.557` n `230`; crypto_major avg `0.7655` n `8`; equity avg `-0.0837` n `102`; fx avg `0.0203` n `6`; index avg `0.0993` n `25`; metal avg `0.1828` n `20`; unknown avg `0.9266` n `778`
- 24h: commodity avg `0.593` n `12`; crypto_alt avg `-2.1374` n `230`; crypto_major avg `-0.2655` n `8`; equity avg `-3.6123` n `102`; fx avg `0.0281` n `6`; index avg `-0.6118` n `25`; metal avg `0.4067` n `20`; unknown avg `-0.7216` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
