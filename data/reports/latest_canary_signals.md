# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T02:37:25.436327+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0214` n `12`; crypto_alt avg `-0.1966` n `230`; crypto_major avg `-0.2133` n `8`; equity avg `-0.5673` n `102`; fx avg `-0.0129` n `6`; index avg `-0.1003` n `25`; metal avg `-0.0751` n `20`; unknown avg `0.0158` n `779`
- 1h: commodity avg `-0.0331` n `12`; crypto_alt avg `0.0172` n `230`; crypto_major avg `-0.0383` n `8`; equity avg `-1.082` n `102`; fx avg `-0.0216` n `6`; index avg `-0.1976` n `25`; metal avg `-0.1489` n `20`; unknown avg `-0.0691` n `779`
- 4h: commodity avg `-0.148` n `12`; crypto_alt avg `0.7106` n `230`; crypto_major avg `0.3724` n `8`; equity avg `0.3873` n `102`; fx avg `-0.0381` n `6`; index avg `0.1398` n `25`; metal avg `-0.0504` n `20`; unknown avg `-0.0754` n `778`
- 24h: commodity avg `0.4678` n `12`; crypto_alt avg `-1.0805` n `230`; crypto_major avg `-0.191` n `8`; equity avg `-2.2018` n `102`; fx avg `0.0305` n `6`; index avg `-0.1023` n `25`; metal avg `0.1686` n `20`; unknown avg `-0.6083` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
