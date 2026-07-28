# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T12:27:15.959860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `0.115` n `230`; crypto_major avg `0.0453` n `8`; equity avg `0.1464` n `102`; fx avg `-0.0002` n `6`; index avg `0.0301` n `25`; metal avg `0.0538` n `20`; unknown avg `-0.0169` n `774`
- 1h: commodity avg `0.0904` n `12`; crypto_alt avg `0.0386` n `230`; crypto_major avg `0.0196` n `8`; equity avg `0.2409` n `102`; fx avg `0.0095` n `6`; index avg `0.0938` n `25`; metal avg `0.0832` n `20`; unknown avg `-0.0277` n `774`
- 4h: commodity avg `0.1583` n `12`; crypto_alt avg `0.0919` n `230`; crypto_major avg `-0.1728` n `8`; equity avg `-0.4004` n `102`; fx avg `-0.0305` n `6`; index avg `0.0227` n `25`; metal avg `-0.1284` n `20`; unknown avg `-0.1336` n `774`
- 24h: commodity avg `-0.6271` n `12`; crypto_alt avg `-3.3523` n `230`; crypto_major avg `-3.4819` n `8`; equity avg `-4.0323` n `102`; fx avg `-0.1576` n `6`; index avg `-0.77` n `25`; metal avg `-0.46` n `20`; unknown avg `1225.279` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
