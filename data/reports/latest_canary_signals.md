# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T19:52:26.688179+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `0.0637` n `230`; crypto_major avg `0.0452` n `8`; equity avg `0.0056` n `121`; fx avg `-0.003` n `6`; index avg `0.0105` n `25`; metal avg `0.0543` n `20`; unknown avg `-0.0601` n `793`
- 1h: commodity avg `-0.0979` n `12`; crypto_alt avg `-0.2042` n `230`; crypto_major avg `0.1677` n `8`; equity avg `0.0251` n `121`; fx avg `-0.0056` n `6`; index avg `0.0072` n `25`; metal avg `0.0123` n `20`; unknown avg `0.9668` n `793`
- 4h: commodity avg `-0.0761` n `12`; crypto_alt avg `-0.9131` n `230`; crypto_major avg `-0.6166` n `8`; equity avg `-0.3271` n `121`; fx avg `0.0226` n `6`; index avg `-0.0792` n `25`; metal avg `0.0513` n `20`; unknown avg `1.0657` n `793`
- 24h: commodity avg `0.0709` n `12`; crypto_alt avg `6.7655` n `230`; crypto_major avg `4.9251` n `8`; equity avg `1.0613` n `121`; fx avg `-0.0939` n `6`; index avg `0.1128` n `25`; metal avg `0.5427` n `20`; unknown avg `2.2618` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1754`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
