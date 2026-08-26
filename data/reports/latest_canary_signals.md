# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T09:37:24.397664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0565` n `12`; crypto_alt avg `-0.0717` n `231`; crypto_major avg `-0.0249` n `8`; equity avg `-0.0078` n `122`; fx avg `0.0056` n `6`; index avg `-0.0` n `25`; metal avg `0.0004` n `20`; unknown avg `0.012` n `797`
- 1h: commodity avg `0.0927` n `12`; crypto_alt avg `-0.7942` n `231`; crypto_major avg `-0.6595` n `8`; equity avg `-0.0846` n `122`; fx avg `-0.0057` n `6`; index avg `-0.0111` n `25`; metal avg `-0.0388` n `20`; unknown avg `-0.08` n `797`
- 4h: commodity avg `-0.0923` n `12`; crypto_alt avg `-0.7141` n `231`; crypto_major avg `-0.8382` n `8`; equity avg `-0.2447` n `122`; fx avg `-0.0178` n `6`; index avg `-0.037` n `25`; metal avg `-0.1438` n `20`; unknown avg `-0.0023` n `781`
- 24h: commodity avg `-0.2528` n `12`; crypto_alt avg `-2.5621` n `231`; crypto_major avg `-2.5269` n `8`; equity avg `0.0977` n `122`; fx avg `-0.0457` n `6`; index avg `-0.043` n `25`; metal avg `0.1525` n `20`; unknown avg `0.6289` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
