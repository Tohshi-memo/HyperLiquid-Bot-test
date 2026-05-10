# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T09:16:55.826035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `-0.0558` n `228`; crypto_major avg `-0.0376` n `8`; equity avg `-0.0101` n `65`; fx avg `0.0` n `5`; index avg `-0.0047` n `23`; metal avg `0.0102` n `18`; unknown avg `-0.1782` n `376`
- 1h: commodity avg `-0.0387` n `12`; crypto_alt avg `0.1473` n `228`; crypto_major avg `0.1964` n `8`; equity avg `0.0195` n `65`; fx avg `0.0017` n `5`; index avg `-0.0003` n `23`; metal avg `0.0346` n `18`; unknown avg `0.0208` n `376`
- 4h: commodity avg `-0.1442` n `12`; crypto_alt avg `0.5805` n `228`; crypto_major avg `0.3975` n `8`; equity avg `0.0298` n `65`; fx avg `0.0072` n `5`; index avg `-0.0147` n `23`; metal avg `-0.0084` n `18`; unknown avg `0.0038` n `366`
- 24h: commodity avg `0.0442` n `12`; crypto_alt avg `0.0194` n `228`; crypto_major avg `-0.0083` n `8`; equity avg `0.9863` n `65`; fx avg `-0.0193` n `5`; index avg `0.2028` n `23`; metal avg `0.3703` n `18`; unknown avg `0.063` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
