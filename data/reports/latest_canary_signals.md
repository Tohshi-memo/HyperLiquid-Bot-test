# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T00:22:29.426950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1442` n `12`; crypto_alt avg `0.0835` n `230`; crypto_major avg `0.015` n `8`; equity avg `0.1767` n `102`; fx avg `-0.0432` n `6`; index avg `0.0183` n `25`; metal avg `-0.0654` n `20`; unknown avg `-0.0306` n `778`
- 1h: commodity avg `-0.1899` n `12`; crypto_alt avg `0.1505` n `230`; crypto_major avg `0.1869` n `8`; equity avg `0.5796` n `102`; fx avg `-0.0784` n `6`; index avg `0.053` n `25`; metal avg `-0.1109` n `20`; unknown avg `0.0213` n `778`
- 4h: commodity avg `-0.2581` n `12`; crypto_alt avg `0.8005` n `230`; crypto_major avg `0.7507` n `8`; equity avg `0.7979` n `102`; fx avg `-0.0425` n `6`; index avg `0.2432` n `25`; metal avg `0.2504` n `20`; unknown avg `0.8597` n `778`
- 24h: commodity avg `0.5528` n `12`; crypto_alt avg `-2.252` n `230`; crypto_major avg `-0.4294` n `8`; equity avg `-4.1002` n `102`; fx avg `-0.0601` n `6`; index avg `-0.7036` n `25`; metal avg `0.266` n `20`; unknown avg `-0.7599` n `761`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
