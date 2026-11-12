# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T20:37:27.369945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0319` n `13`; crypto_alt avg `0.0133` n `239`; crypto_major avg `-0.1268` n `8`; equity avg `-0.2747` n `162`; fx avg `0.0126` n `6`; index avg `-0.0314` n `27`; metal avg `-0.0571` n `20`; unknown avg `0.4062` n `1261`
- 1h: commodity avg `0.0191` n `13`; crypto_alt avg `0.2485` n `239`; crypto_major avg `0.1317` n `8`; equity avg `-0.2913` n `162`; fx avg `0.009` n `6`; index avg `-0.017` n `27`; metal avg `-0.0231` n `20`; unknown avg `1.8805` n `1241`
- 4h: commodity avg `0.5693` n `13`; crypto_alt avg `0.3915` n `239`; crypto_major avg `0.2243` n `8`; equity avg `-0.8037` n `162`; fx avg `-0.0028` n `6`; index avg `-0.0793` n `27`; metal avg `0.0329` n `20`; unknown avg `69.7244` n `1231`
- 24h: commodity avg `0.9379` n `13`; crypto_alt avg `-2.5384` n `239`; crypto_major avg `-3.0591` n `8`; equity avg `-2.9191` n `162`; fx avg `-0.1352` n `6`; index avg `-0.1863` n `27`; metal avg `-0.7578` n `20`; unknown avg `30.8047` n `1137`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
