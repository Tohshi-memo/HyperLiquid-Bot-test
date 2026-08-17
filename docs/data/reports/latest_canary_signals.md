# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T23:41:51.566707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `0.0063` n `230`; crypto_major avg `0.12` n `8`; equity avg `0.0643` n `114`; fx avg `0.005` n `6`; index avg `0.0037` n `25`; metal avg `0.027` n `20`; unknown avg `-0.081` n `793`
- 1h: commodity avg `-0.0273` n `12`; crypto_alt avg `0.0119` n `230`; crypto_major avg `0.2453` n `8`; equity avg `-0.048` n `114`; fx avg `-0.0208` n `6`; index avg `-0.0137` n `25`; metal avg `0.0436` n `20`; unknown avg `-0.1574` n `793`
- 4h: commodity avg `0.0928` n `12`; crypto_alt avg `-0.2765` n `230`; crypto_major avg `0.2304` n `8`; equity avg `-0.0015` n `114`; fx avg `-0.0124` n `6`; index avg `-0.0054` n `25`; metal avg `0.0196` n `20`; unknown avg `-0.2766` n `792`
- 24h: commodity avg `0.5515` n `12`; crypto_alt avg `0.471` n `230`; crypto_major avg `1.6881` n `8`; equity avg `1.1854` n `114`; fx avg `0.0088` n `6`; index avg `0.0463` n `25`; metal avg `0.2621` n `20`; unknown avg `0.3052` n `776`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
