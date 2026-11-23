# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T06:07:25.596039+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1057` n `13`; crypto_alt avg `0.0633` n `239`; crypto_major avg `-0.0003` n `8`; equity avg `0.0896` n `166`; fx avg `0.0202` n `6`; index avg `-0.0174` n `27`; metal avg `0.0237` n `20`; unknown avg `0.0154` n `1238`
- 1h: commodity avg `-0.0829` n `13`; crypto_alt avg `0.6692` n `239`; crypto_major avg `0.6854` n `8`; equity avg `0.8151` n `166`; fx avg `0.0171` n `6`; index avg `0.0472` n `27`; metal avg `0.2555` n `20`; unknown avg `0.9436` n `1236`
- 4h: commodity avg `-0.0454` n `13`; crypto_alt avg `1.469` n `239`; crypto_major avg `1.5597` n `8`; equity avg `0.9807` n `166`; fx avg `0.037` n `6`; index avg `-0.019` n `27`; metal avg `0.384` n `20`; unknown avg `164.3577` n `1221`
- 24h: commodity avg `-0.3954` n `13`; crypto_alt avg `2.5348` n `239`; crypto_major avg `3.405` n `8`; equity avg `2.7826` n `166`; fx avg `0.2351` n `6`; index avg `0.2061` n `27`; metal avg `0.6105` n `20`; unknown avg `295.1044` n `1017`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
