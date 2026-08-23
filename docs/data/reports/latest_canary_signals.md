# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T09:52:24.801940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `0.2334` n `230`; crypto_major avg `0.1892` n `8`; equity avg `0.0167` n `121`; fx avg `0.0097` n `6`; index avg `0.0083` n `25`; metal avg `-0.0001` n `20`; unknown avg `0.0863` n `794`
- 1h: commodity avg `-0.0019` n `12`; crypto_alt avg `0.4336` n `230`; crypto_major avg `-0.0001` n `8`; equity avg `0.0311` n `121`; fx avg `0.0089` n `6`; index avg `0.0118` n `25`; metal avg `-0.0252` n `20`; unknown avg `-0.0288` n `794`
- 4h: commodity avg `-0.0228` n `12`; crypto_alt avg `2.4322` n `230`; crypto_major avg `1.224` n `8`; equity avg `0.1936` n `121`; fx avg `-0.007` n `6`; index avg `0.008` n `25`; metal avg `-0.0288` n `20`; unknown avg `0.4559` n `778`
- 24h: commodity avg `-0.0211` n `12`; crypto_alt avg `-1.2785` n `230`; crypto_major avg `-0.0582` n `8`; equity avg `0.2279` n `121`; fx avg `0.0636` n `6`; index avg `0.0239` n `25`; metal avg `0.0182` n `20`; unknown avg `2.5272` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
