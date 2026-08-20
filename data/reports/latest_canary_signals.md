# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T07:22:37.863592+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0636` n `12`; crypto_alt avg `-0.0438` n `230`; crypto_major avg `-0.1184` n `8`; equity avg `-0.074` n `121`; fx avg `0.0185` n `6`; index avg `-0.0208` n `25`; metal avg `-0.0336` n `20`; unknown avg `0.0768` n `792`
- 1h: commodity avg `0.1297` n `12`; crypto_alt avg `0.1962` n `230`; crypto_major avg `0.3512` n `8`; equity avg `0.0351` n `121`; fx avg `0.0404` n `6`; index avg `-0.0079` n `25`; metal avg `-0.1123` n `20`; unknown avg `0.2625` n `792`
- 4h: commodity avg `0.1651` n `12`; crypto_alt avg `0.7945` n `230`; crypto_major avg `1.2702` n `8`; equity avg `0.1488` n `121`; fx avg `0.0237` n `6`; index avg `0.0033` n `25`; metal avg `-0.1013` n `20`; unknown avg `0.3492` n `776`
- 24h: commodity avg `0.0685` n `12`; crypto_alt avg `5.7812` n `230`; crypto_major avg `10.4385` n `8`; equity avg `0.7375` n `120`; fx avg `0.0755` n `6`; index avg `0.1963` n `25`; metal avg `0.9545` n `20`; unknown avg `2.0223` n `773`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1988`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
