# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T22:43:42.785873+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `-0.0634` n `230`; crypto_major avg `-0.073` n `8`; equity avg `0.1119` n `102`; fx avg `0.0066` n `6`; index avg `0.0217` n `25`; metal avg `0.0302` n `20`; unknown avg `0.8278` n `778`
- 1h: commodity avg `-0.1632` n `12`; crypto_alt avg `0.4896` n `230`; crypto_major avg `0.529` n `8`; equity avg `1.4068` n `102`; fx avg `0.0251` n `6`; index avg `0.2335` n `25`; metal avg `0.162` n `20`; unknown avg `1.8707` n `778`
- 4h: commodity avg `-0.0804` n `12`; crypto_alt avg `-0.4615` n `230`; crypto_major avg `-0.3958` n `8`; equity avg `-1.787` n `102`; fx avg `0.0785` n `6`; index avg `-0.4047` n `25`; metal avg `0.0741` n `20`; unknown avg `0.1386` n `778`
- 24h: commodity avg `0.5448` n `12`; crypto_alt avg `-2.2995` n `230`; crypto_major avg `-0.4325` n `8`; equity avg `-3.4519` n `102`; fx avg `0.0467` n `6`; index avg `-0.5778` n `25`; metal avg `0.3981` n `20`; unknown avg `-0.6513` n `760`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
