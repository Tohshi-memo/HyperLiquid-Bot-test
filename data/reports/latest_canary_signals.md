# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T19:52:31.787138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0566` n `12`; crypto_alt avg `-0.0464` n `230`; crypto_major avg `-0.0928` n `8`; equity avg `-0.0796` n `102`; fx avg `-0.0069` n `6`; index avg `-0.0293` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.2122` n `774`
- 1h: commodity avg `-0.0891` n `12`; crypto_alt avg `0.3542` n `230`; crypto_major avg `0.4358` n `8`; equity avg `0.5931` n `102`; fx avg `-0.0102` n `6`; index avg `0.0919` n `25`; metal avg `0.1169` n `20`; unknown avg `95.9848` n `774`
- 4h: commodity avg `-0.2768` n `12`; crypto_alt avg `0.3227` n `230`; crypto_major avg `0.435` n `8`; equity avg `1.0659` n `102`; fx avg `-0.0372` n `6`; index avg `0.1461` n `25`; metal avg `0.0572` n `20`; unknown avg `95.7206` n `774`
- 24h: commodity avg `-1.0267` n `12`; crypto_alt avg `-1.0099` n `230`; crypto_major avg `-0.2391` n `8`; equity avg `-1.1514` n `102`; fx avg `-0.0315` n `6`; index avg `-0.3554` n `25`; metal avg `0.239` n `20`; unknown avg `97.6904` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1846`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
