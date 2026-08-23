# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T10:37:25.665841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `12`; crypto_alt avg `0.1528` n `230`; crypto_major avg `-0.0838` n `8`; equity avg `0.0142` n `121`; fx avg `0.0019` n `6`; index avg `-0.002` n `25`; metal avg `-0.0005` n `20`; unknown avg `0.0589` n `795`
- 1h: commodity avg `0.0133` n `12`; crypto_alt avg `0.8504` n `230`; crypto_major avg `0.5659` n `8`; equity avg `0.0613` n `121`; fx avg `0.0082` n `6`; index avg `0.0208` n `25`; metal avg `0.0134` n `20`; unknown avg `0.2054` n `794`
- 4h: commodity avg `-0.0152` n `12`; crypto_alt avg `2.4378` n `230`; crypto_major avg `1.2065` n `8`; equity avg `0.2396` n `121`; fx avg `-0.0609` n `6`; index avg `0.039` n `25`; metal avg `0.0027` n `20`; unknown avg `0.38` n `794`
- 24h: commodity avg `0.0006` n `12`; crypto_alt avg `-0.3059` n `230`; crypto_major avg `0.4632` n `8`; equity avg `0.3204` n `121`; fx avg `0.0464` n `6`; index avg `0.0449` n `25`; metal avg `0.0257` n `20`; unknown avg `2.7791` n `778`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
