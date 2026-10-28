# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T10:37:29.787539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.44` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.037` n `13`; crypto_alt avg `-0.1061` n `238`; crypto_major avg `-0.0784` n `8`; equity avg `0.1173` n `154`; fx avg `0.0026` n `6`; index avg `0.0208` n `27`; metal avg `-0.0022` n `20`; unknown avg `1.3382` n `1239`
- 1h: commodity avg `0.0336` n `13`; crypto_alt avg `0.1156` n `238`; crypto_major avg `0.253` n `8`; equity avg `0.3999` n `154`; fx avg `-0.0067` n `6`; index avg `0.0471` n `27`; metal avg `-0.0903` n `20`; unknown avg `1.3495` n `1233`
- 4h: commodity avg `-0.0864` n `13`; crypto_alt avg `0.3837` n `238`; crypto_major avg `0.7262` n `8`; equity avg `0.2587` n `154`; fx avg `0.0291` n `6`; index avg `0.0398` n `27`; metal avg `-0.0041` n `20`; unknown avg `92.5827` n `1186`
- 24h: commodity avg `-0.1305` n `13`; crypto_alt avg `2.8191` n `238`; crypto_major avg `3.0548` n `8`; equity avg `3.8756` n `154`; fx avg `0.0873` n `6`; index avg `0.5166` n `27`; metal avg `0.3142` n `20`; unknown avg `8.4157` n `1024`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
