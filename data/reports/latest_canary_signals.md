# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T14:07:27.635917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.44` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0579` n `13`; crypto_alt avg `-0.0916` n `239`; crypto_major avg `-0.0018` n `8`; equity avg `-0.1517` n `163`; fx avg `-0.0071` n `6`; index avg `-0.0182` n `27`; metal avg `0.0067` n `20`; unknown avg `-0.0607` n `1260`
- 1h: commodity avg `-0.0525` n `13`; crypto_alt avg `0.1336` n `239`; crypto_major avg `-0.0496` n `8`; equity avg `0.2211` n `163`; fx avg `-0.0082` n `6`; index avg `0.0279` n `27`; metal avg `0.1335` n `20`; unknown avg `3.0597` n `1264`
- 4h: commodity avg `0.3772` n `13`; crypto_alt avg `-0.2837` n `239`; crypto_major avg `-0.8551` n `8`; equity avg `-0.9409` n `163`; fx avg `-0.0031` n `6`; index avg `-0.1145` n `27`; metal avg `-0.0111` n `20`; unknown avg `0.4879` n `1256`
- 24h: commodity avg `0.0198` n `13`; crypto_alt avg `-0.3308` n `239`; crypto_major avg `-0.5763` n `8`; equity avg `-0.3663` n `163`; fx avg `-0.1169` n `6`; index avg `-0.0253` n `27`; metal avg `-0.9563` n `20`; unknown avg `0.2856` n `1135`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
