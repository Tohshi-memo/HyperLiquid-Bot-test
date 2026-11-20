# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T08:07:38.352609+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0217` n `13`; crypto_alt avg `0.0421` n `239`; crypto_major avg `-0.0423` n `8`; equity avg `0.0982` n `165`; fx avg `-0.0031` n `6`; index avg `0.0185` n `27`; metal avg `-0.0279` n `20`; unknown avg `3.6278` n `1206`
- 1h: commodity avg `-0.0719` n `13`; crypto_alt avg `0.1791` n `239`; crypto_major avg `0.0239` n `8`; equity avg `0.4368` n `165`; fx avg `-0.0234` n `6`; index avg `0.0724` n `27`; metal avg `0.1762` n `20`; unknown avg `4.2535` n `1206`
- 4h: commodity avg `-0.2323` n `13`; crypto_alt avg `0.5899` n `239`; crypto_major avg `0.4538` n `8`; equity avg `-0.346` n `165`; fx avg `-0.0178` n `6`; index avg `0.0555` n `27`; metal avg `0.2879` n `20`; unknown avg `-0.227` n `1180`
- 24h: commodity avg `-0.1779` n `13`; crypto_alt avg `-2.8971` n `239`; crypto_major avg `-2.4341` n `8`; equity avg `-6.6505` n `165`; fx avg `-0.0398` n `6`; index avg `-0.5887` n `27`; metal avg `-1.3942` n `20`; unknown avg `19.2138` n `1159`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
