# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T03:07:27.270097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0236` n `12`; crypto_alt avg `-0.0275` n `230`; crypto_major avg `-0.0706` n `8`; equity avg `-0.2261` n `102`; fx avg `0.0175` n `6`; index avg `-0.0403` n `25`; metal avg `-0.0362` n `20`; unknown avg `0.0284` n `779`
- 1h: commodity avg `-0.0739` n `12`; crypto_alt avg `-0.0969` n `230`; crypto_major avg `-0.2354` n `8`; equity avg `-1.0716` n `102`; fx avg `-0.0168` n `6`; index avg `-0.2431` n `25`; metal avg `-0.1935` n `20`; unknown avg `-0.0306` n `779`
- 4h: commodity avg `-0.1792` n `12`; crypto_alt avg `0.7664` n `230`; crypto_major avg `0.427` n `8`; equity avg `0.3183` n `102`; fx avg `-0.0265` n `6`; index avg `0.0717` n `25`; metal avg `-0.2262` n `20`; unknown avg `0.0982` n `778`
- 24h: commodity avg `0.3896` n `12`; crypto_alt avg `-0.6602` n `230`; crypto_major avg `0.0267` n `8`; equity avg `-2.0338` n `102`; fx avg `0.0507` n `6`; index avg `-0.0922` n `25`; metal avg `0.1648` n `20`; unknown avg `-0.5828` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
