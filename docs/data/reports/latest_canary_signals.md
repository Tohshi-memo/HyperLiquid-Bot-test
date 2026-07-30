# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T00:37:27.113145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1278` n `12`; crypto_alt avg `-0.3049` n `230`; crypto_major avg `-0.35` n `8`; equity avg `-0.1491` n `102`; fx avg `0.0094` n `6`; index avg `-0.0671` n `25`; metal avg `-0.0739` n `20`; unknown avg `0.0494` n `778`
- 1h: commodity avg `-0.0289` n `12`; crypto_alt avg `-0.0826` n `230`; crypto_major avg `-0.1452` n `8`; equity avg `0.3201` n `102`; fx avg `-0.0635` n `6`; index avg `-0.0104` n `25`; metal avg `-0.1887` n `20`; unknown avg `-0.1092` n `778`
- 4h: commodity avg `-0.1085` n `12`; crypto_alt avg `0.5983` n `230`; crypto_major avg `0.3238` n `8`; equity avg `0.6895` n `102`; fx avg `-0.0293` n `6`; index avg `0.1083` n `25`; metal avg `0.0616` n `20`; unknown avg `0.5617` n `778`
- 24h: commodity avg `0.5493` n `12`; crypto_alt avg `-2.3671` n `230`; crypto_major avg `-0.7203` n `8`; equity avg `-3.6985` n `102`; fx avg `-0.0383` n `6`; index avg `-0.6816` n `25`; metal avg `0.1698` n `20`; unknown avg `-0.7561` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
