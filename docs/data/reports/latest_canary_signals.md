# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T03:37:29.759538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `0.0612` n `230`; crypto_major avg `0.1645` n `8`; equity avg `0.0011` n `121`; fx avg `0.028` n `6`; index avg `0.0072` n `25`; metal avg `-0.0219` n `20`; unknown avg `-0.0576` n `793`
- 1h: commodity avg `-0.0726` n `12`; crypto_alt avg `0.0815` n `230`; crypto_major avg `-0.4074` n `8`; equity avg `-0.226` n `121`; fx avg `0.0351` n `6`; index avg `-0.0015` n `25`; metal avg `-0.0159` n `20`; unknown avg `0.81` n `793`
- 4h: commodity avg `0.0308` n `12`; crypto_alt avg `0.7428` n `230`; crypto_major avg `0.9528` n `8`; equity avg `0.7994` n `121`; fx avg `-0.0992` n `6`; index avg `0.1624` n `25`; metal avg `0.1754` n `20`; unknown avg `-0.0942` n `793`
- 24h: commodity avg `0.3357` n `12`; crypto_alt avg `5.8161` n `230`; crypto_major avg `7.1947` n `8`; equity avg `-0.3025` n `121`; fx avg `-0.0035` n `6`; index avg `-0.0423` n `25`; metal avg `0.4773` n `20`; unknown avg `2.6248` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1844`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1809`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
