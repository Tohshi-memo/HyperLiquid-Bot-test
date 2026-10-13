# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T21:37:38.160103+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `13`; crypto_alt avg `0.2694` n `235`; crypto_major avg `0.0935` n `8`; equity avg `0.0685` n `151`; fx avg `-0.0035` n `6`; index avg `0.0012` n `26`; metal avg `0.0098` n `20`; unknown avg `3.9746` n `1135`
- 1h: commodity avg `-0.0469` n `13`; crypto_alt avg `0.0508` n `235`; crypto_major avg `0.0153` n `8`; equity avg `0.0847` n `151`; fx avg `-0.0174` n `6`; index avg `0.0211` n `26`; metal avg `0.0443` n `20`; unknown avg `3.7816` n `1127`
- 4h: commodity avg `0.1828` n `13`; crypto_alt avg `0.6238` n `235`; crypto_major avg `0.1971` n `8`; equity avg `0.4893` n `151`; fx avg `-0.0084` n `6`; index avg `0.0599` n `26`; metal avg `0.0222` n `20`; unknown avg `5.0267` n `1075`
- 24h: commodity avg `0.8471` n `13`; crypto_alt avg `-0.9341` n `235`; crypto_major avg `-0.3495` n `8`; equity avg `-0.5873` n `151`; fx avg `0.1623` n `6`; index avg `-0.126` n `26`; metal avg `-0.2746` n `20`; unknown avg `2.427` n `1003`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1576`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1428`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1175`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0912`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0811`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
