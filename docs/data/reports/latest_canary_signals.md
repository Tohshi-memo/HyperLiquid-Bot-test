# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T06:22:23.769548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `0.3153` n `230`; crypto_major avg `0.317` n `8`; equity avg `-0.0045` n `121`; fx avg `-0.0353` n `6`; index avg `-0.0005` n `25`; metal avg `0.024` n `20`; unknown avg `0.1288` n `792`
- 1h: commodity avg `0.0147` n `12`; crypto_alt avg `0.0699` n `230`; crypto_major avg `0.1703` n `8`; equity avg `-0.016` n `121`; fx avg `-0.019` n `6`; index avg `0.0106` n `25`; metal avg `0.0525` n `20`; unknown avg `0.0658` n `776`
- 4h: commodity avg `0.0226` n `12`; crypto_alt avg `0.1645` n `230`; crypto_major avg `0.2128` n `8`; equity avg `0.1113` n `121`; fx avg `-0.0008` n `6`; index avg `0.0259` n `25`; metal avg `0.0476` n `20`; unknown avg `0.0651` n `776`
- 24h: commodity avg `-0.0392` n `12`; crypto_alt avg `5.6315` n `230`; crypto_major avg `10.1819` n `8`; equity avg `1.6119` n `120`; fx avg `0.0443` n `6`; index avg `0.363` n `25`; metal avg `1.0792` n `20`; unknown avg `1.7397` n `773`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
