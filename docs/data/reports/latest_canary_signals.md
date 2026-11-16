# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T06:52:27.856752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0845` n `13`; crypto_alt avg `0.1675` n `239`; crypto_major avg `0.1687` n `8`; equity avg `0.1314` n `162`; fx avg `-0.0238` n `6`; index avg `0.0134` n `27`; metal avg `0.016` n `20`; unknown avg `-0.0141` n `1227`
- 1h: commodity avg `0.0674` n `13`; crypto_alt avg `0.0761` n `239`; crypto_major avg `0.2046` n `8`; equity avg `0.1527` n `162`; fx avg `-0.0038` n `6`; index avg `0.0217` n `27`; metal avg `0.0313` n `20`; unknown avg `0.1575` n `1205`
- 4h: commodity avg `0.2618` n `13`; crypto_alt avg `-0.7709` n `239`; crypto_major avg `-0.5271` n `8`; equity avg `-0.917` n `162`; fx avg `-0.0519` n `6`; index avg `-0.0913` n `27`; metal avg `-0.0675` n `20`; unknown avg `0.2404` n `1193`
- 24h: commodity avg `-0.2407` n `13`; crypto_alt avg `-0.2836` n `239`; crypto_major avg `0.646` n `8`; equity avg `-0.3414` n `162`; fx avg `-0.0733` n `6`; index avg `-0.0294` n `27`; metal avg `0.098` n `20`; unknown avg `0.7466` n `1123`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
