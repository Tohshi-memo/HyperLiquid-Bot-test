# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T00:52:32.109154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.0791` n `230`; crypto_major avg `0.0084` n `8`; equity avg `-0.1052` n `114`; fx avg `-0.0046` n `6`; index avg `-0.007` n `25`; metal avg `-0.0368` n `20`; unknown avg `0.0764` n `793`
- 1h: commodity avg `-0.0248` n `12`; crypto_alt avg `-0.0496` n `230`; crypto_major avg `-0.0885` n `8`; equity avg `0.1872` n `114`; fx avg `-0.0344` n `6`; index avg `0.0424` n `25`; metal avg `0.0582` n `20`; unknown avg `0.0582` n `793`
- 4h: commodity avg `-0.0429` n `12`; crypto_alt avg `-0.1813` n `230`; crypto_major avg `0.2152` n `8`; equity avg `0.2848` n `114`; fx avg `-0.0494` n `6`; index avg `0.0486` n `25`; metal avg `0.0981` n `20`; unknown avg `-0.1139` n `792`
- 24h: commodity avg `0.5905` n `12`; crypto_alt avg `0.5442` n `230`; crypto_major avg `1.6294` n `8`; equity avg `1.2515` n `114`; fx avg `0.0195` n `6`; index avg `0.0843` n `25`; metal avg `0.1591` n `20`; unknown avg `0.3522` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.21`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
