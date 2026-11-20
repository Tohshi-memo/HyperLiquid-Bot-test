# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T11:22:29.385214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0655` n `13`; crypto_alt avg `-0.2088` n `239`; crypto_major avg `-0.2503` n `8`; equity avg `-0.3436` n `165`; fx avg `0.0044` n `6`; index avg `-0.0421` n `27`; metal avg `-0.0577` n `20`; unknown avg `198.213` n `1260`
- 1h: commodity avg `0.2716` n `13`; crypto_alt avg `-0.1295` n `239`; crypto_major avg `-0.0681` n `8`; equity avg `-0.1685` n `165`; fx avg `0.021` n `6`; index avg `-0.0442` n `27`; metal avg `0.0907` n `20`; unknown avg `220.6664` n `1258`
- 4h: commodity avg `-0.1917` n `13`; crypto_alt avg `-0.3439` n `239`; crypto_major avg `-0.5647` n `8`; equity avg `-0.5344` n `165`; fx avg `-0.0275` n `6`; index avg `-0.0515` n `27`; metal avg `0.3568` n `20`; unknown avg `46.5787` n `1194`
- 24h: commodity avg `-0.3107` n `13`; crypto_alt avg `-3.6981` n `239`; crypto_major avg `-3.2605` n `8`; equity avg `-8.0167` n `165`; fx avg `-0.1035` n `6`; index avg `-0.8215` n `27`; metal avg `-1.2457` n `20`; unknown avg `57.4169` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
