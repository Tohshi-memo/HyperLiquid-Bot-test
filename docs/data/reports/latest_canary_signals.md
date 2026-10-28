# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T09:22:35.984865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.6` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0087` n `13`; crypto_alt avg `0.1847` n `238`; crypto_major avg `0.0912` n `8`; equity avg `0.1057` n `154`; fx avg `0.0072` n `6`; index avg `0.0141` n `27`; metal avg `0.0349` n `20`; unknown avg `0.0374` n `1222`
- 1h: commodity avg `-0.0314` n `13`; crypto_alt avg `0.3158` n `238`; crypto_major avg `0.2694` n `8`; equity avg `-0.0259` n `154`; fx avg `0.0016` n `6`; index avg `-0.0029` n `27`; metal avg `0.0253` n `20`; unknown avg `85.0678` n `1218`
- 4h: commodity avg `-0.0172` n `13`; crypto_alt avg `0.2749` n `238`; crypto_major avg `0.5243` n `8`; equity avg `0.0904` n `154`; fx avg `-0.0128` n `6`; index avg `0.0209` n `27`; metal avg `0.0806` n `20`; unknown avg `41.346` n `1182`
- 24h: commodity avg `-0.2584` n `13`; crypto_alt avg `2.2688` n `238`; crypto_major avg `2.6436` n `8`; equity avg `3.5832` n `154`; fx avg `0.1073` n `6`; index avg `0.4534` n `27`; metal avg `0.4357` n `20`; unknown avg `16.092` n `1026`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1771`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
