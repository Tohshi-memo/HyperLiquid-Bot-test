# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T10:07:26.435989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0849` n `13`; crypto_alt avg `0.1567` n `239`; crypto_major avg `0.0058` n `8`; equity avg `0.0859` n `161`; fx avg `0.044` n `6`; index avg `-0.0038` n `27`; metal avg `0.0397` n `20`; unknown avg `18.9355` n `1257`
- 1h: commodity avg `0.2716` n `13`; crypto_alt avg `0.2038` n `239`; crypto_major avg `0.081` n `8`; equity avg `0.0545` n `161`; fx avg `0.0177` n `6`; index avg `-0.0276` n `27`; metal avg `0.1116` n `20`; unknown avg `0.0245` n `1239`
- 4h: commodity avg `0.2228` n `13`; crypto_alt avg `-0.2985` n `239`; crypto_major avg `-0.2532` n `8`; equity avg `0.4602` n `161`; fx avg `-0.0448` n `6`; index avg `-0.0092` n `27`; metal avg `0.1489` n `20`; unknown avg `0.0215` n `1217`
- 24h: commodity avg `0.9618` n `13`; crypto_alt avg `-0.8424` n `239`; crypto_major avg `-1.8061` n `8`; equity avg `1.8645` n `161`; fx avg `-0.2155` n `6`; index avg `0.2017` n `27`; metal avg `0.2679` n `20`; unknown avg `2.2808` n `1175`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.2126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
