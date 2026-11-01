# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T22:52:27.833565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0174` n `13`; crypto_alt avg `0.1439` n `238`; crypto_major avg `0.1572` n `8`; equity avg `0.0219` n `156`; fx avg `0.0033` n `6`; index avg `-0.0005` n `27`; metal avg `0.0123` n `20`; unknown avg `0.0217` n `1249`
- 1h: commodity avg `0.0323` n `13`; crypto_alt avg `-0.2649` n `238`; crypto_major avg `-0.2522` n `8`; equity avg `-0.1075` n `156`; fx avg `0.0232` n `6`; index avg `0.008` n `27`; metal avg `-0.0094` n `20`; unknown avg `0.1967` n `1233`
- 4h: commodity avg `0.0541` n `13`; crypto_alt avg `-0.2532` n `238`; crypto_major avg `-0.2373` n `8`; equity avg `-0.0091` n `156`; fx avg `-0.0204` n `6`; index avg `-0.0148` n `27`; metal avg `-0.0223` n `20`; unknown avg `13.1355` n `1191`
- 24h: commodity avg `0.0306` n `13`; crypto_alt avg `-0.6418` n `238`; crypto_major avg `-0.1394` n `8`; equity avg `0.289` n `156`; fx avg `-0.0143` n `6`; index avg `0.0587` n `27`; metal avg `0.0227` n `20`; unknown avg `3.7963` n `1084`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
