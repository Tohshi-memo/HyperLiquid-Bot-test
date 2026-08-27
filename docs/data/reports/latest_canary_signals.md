# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T21:37:28.055519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0122` n `12`; crypto_alt avg `-0.2537` n `231`; crypto_major avg `-0.1581` n `8`; equity avg `-0.0711` n `127`; fx avg `0.0031` n `6`; index avg `0.004` n `26`; metal avg `-0.0112` n `20`; unknown avg `0.0707` n `792`
- 1h: commodity avg `0.0079` n `12`; crypto_alt avg `-0.0867` n `231`; crypto_major avg `-0.1482` n `8`; equity avg `-0.2293` n `127`; fx avg `-0.007` n `6`; index avg `0.0017` n `26`; metal avg `-0.0139` n `20`; unknown avg `-0.0234` n `792`
- 4h: commodity avg `0.0186` n `12`; crypto_alt avg `-0.8214` n `231`; crypto_major avg `-0.5004` n `8`; equity avg `-0.1343` n `127`; fx avg `0.0086` n `6`; index avg `-0.0034` n `26`; metal avg `-0.0134` n `20`; unknown avg `0.2466` n `792`
- 24h: commodity avg `0.3305` n `12`; crypto_alt avg `1.9431` n `231`; crypto_major avg `2.9466` n `8`; equity avg `-0.0187` n `127`; fx avg `-0.0426` n `6`; index avg `-0.0542` n `26`; metal avg `0.1764` n `20`; unknown avg `0.8946` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
