# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T08:22:30.501158+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.57` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0254` n `13`; crypto_alt avg `0.0185` n `238`; crypto_major avg `0.0847` n `8`; equity avg `-0.0597` n `154`; fx avg `0.0154` n `6`; index avg `-0.0202` n `27`; metal avg `-0.0018` n `20`; unknown avg `0.296` n `1236`
- 1h: commodity avg `-0.1175` n `13`; crypto_alt avg `0.3583` n `238`; crypto_major avg `0.3355` n `8`; equity avg `-0.0161` n `154`; fx avg `0.0302` n `6`; index avg `-0.0052` n `27`; metal avg `0.0625` n `20`; unknown avg `0.7177` n `1212`
- 4h: commodity avg `0.0227` n `13`; crypto_alt avg `0.154` n `238`; crypto_major avg `0.3415` n `8`; equity avg `0.2345` n `154`; fx avg `-0.0275` n `6`; index avg `0.0297` n `27`; metal avg `0.0315` n `20`; unknown avg `1.8983` n `1192`
- 24h: commodity avg `-0.2962` n `13`; crypto_alt avg `1.738` n `238`; crypto_major avg `2.1996` n `8`; equity avg `3.8275` n `154`; fx avg `0.062` n `6`; index avg `0.5278` n `27`; metal avg `0.4421` n `20`; unknown avg `16.264` n `1024`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1611`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
