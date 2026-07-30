# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T03:37:29.195980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0253` n `12`; crypto_alt avg `-0.0496` n `230`; crypto_major avg `-0.1076` n `8`; equity avg `0.1188` n `102`; fx avg `-0.013` n `6`; index avg `0.0136` n `25`; metal avg `-0.0357` n `20`; unknown avg `-0.0024` n `779`
- 1h: commodity avg `0.0092` n `12`; crypto_alt avg `-0.0724` n `230`; crypto_major avg `-0.1691` n `8`; equity avg `-0.472` n `102`; fx avg `-0.0133` n `6`; index avg `-0.1066` n `25`; metal avg `-0.1949` n `20`; unknown avg `-0.0188` n `779`
- 4h: commodity avg `-0.1297` n `12`; crypto_alt avg `0.5642` n `230`; crypto_major avg `0.1677` n `8`; equity avg `-0.0468` n `102`; fx avg `-0.0425` n `6`; index avg `0.0074` n `25`; metal avg `-0.3434` n `20`; unknown avg `-0.005` n `778`
- 24h: commodity avg `0.414` n `12`; crypto_alt avg `-0.2331` n `230`; crypto_major avg `0.1762` n `8`; equity avg `-1.828` n `102`; fx avg `0.0129` n `6`; index avg `-0.0936` n `25`; metal avg `0.0933` n `20`; unknown avg `-0.5436` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
