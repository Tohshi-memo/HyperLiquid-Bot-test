# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T09:52:28.109047+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.57` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0079` n `13`; crypto_alt avg `0.1836` n `238`; crypto_major avg `0.2337` n `8`; equity avg `0.1047` n `154`; fx avg `-0.0078` n `6`; index avg `0.0198` n `27`; metal avg `-0.0463` n `20`; unknown avg `1.044` n `1237`
- 1h: commodity avg `0.0144` n `13`; crypto_alt avg `0.2176` n `238`; crypto_major avg `0.1622` n `8`; equity avg `-0.0397` n `154`; fx avg `0.0055` n `6`; index avg `0.0021` n `27`; metal avg `-0.0579` n `20`; unknown avg `3.3258` n `1202`
- 4h: commodity avg `-0.0552` n `13`; crypto_alt avg `0.5786` n `238`; crypto_major avg `0.7915` n `8`; equity avg `0.1857` n `154`; fx avg `0.0229` n `6`; index avg `0.0261` n `27`; metal avg `0.0185` n `20`; unknown avg `39.8349` n `1168`
- 24h: commodity avg `-0.1676` n `13`; crypto_alt avg `2.8933` n `238`; crypto_major avg `3.0853` n `8`; equity avg `3.4691` n `154`; fx avg `0.1067` n `6`; index avg `0.4748` n `27`; metal avg `0.3488` n `20`; unknown avg `8.3533` n `1024`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
