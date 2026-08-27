# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T18:52:24.382965+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `0.1008` n `231`; crypto_major avg `0.0583` n `8`; equity avg `0.0811` n `127`; fx avg `0.002` n `6`; index avg `0.0124` n `26`; metal avg `0.0458` n `20`; unknown avg `0.6875` n `792`
- 1h: commodity avg `-0.022` n `12`; crypto_alt avg `-0.6042` n `231`; crypto_major avg `-0.5616` n `8`; equity avg `-0.1462` n `127`; fx avg `0.0009` n `6`; index avg `-0.0571` n `26`; metal avg `-0.0192` n `20`; unknown avg `0.2461` n `792`
- 4h: commodity avg `0.2316` n `12`; crypto_alt avg `-0.1644` n `231`; crypto_major avg `-0.0106` n `8`; equity avg `0.0184` n `127`; fx avg `0.0158` n `6`; index avg `-0.0511` n `26`; metal avg `0.2271` n `20`; unknown avg `0.4897` n `791`
- 24h: commodity avg `0.4618` n `12`; crypto_alt avg `2.8554` n `231`; crypto_major avg `3.8062` n `8`; equity avg `1.4081` n `127`; fx avg `-0.047` n `6`; index avg `0.0879` n `26`; metal avg `0.1875` n `20`; unknown avg `1.1208` n `775`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
