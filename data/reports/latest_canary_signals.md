# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T06:07:34.472834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0805` n `12`; crypto_alt avg `-0.1547` n `231`; crypto_major avg `-0.1794` n `8`; equity avg `0.0924` n `122`; fx avg `-0.0243` n `6`; index avg `0.0136` n `25`; metal avg `0.0617` n `20`; unknown avg `-0.0647` n `778`
- 1h: commodity avg `-0.2012` n `12`; crypto_alt avg `-0.0168` n `231`; crypto_major avg `-0.0227` n `8`; equity avg `0.2998` n `122`; fx avg `0.0134` n `6`; index avg `0.047` n `25`; metal avg `0.0329` n `20`; unknown avg `-0.084` n `778`
- 4h: commodity avg `-0.3329` n `12`; crypto_alt avg `1.0644` n `231`; crypto_major avg `0.999` n `8`; equity avg `1.0101` n `122`; fx avg `-0.003` n `6`; index avg `0.1772` n `25`; metal avg `-0.0472` n `20`; unknown avg `0.0323` n `778`
- 24h: commodity avg `-0.2037` n `12`; crypto_alt avg `2.1853` n `231`; crypto_major avg `3.0748` n `8`; equity avg `0.3661` n `122`; fx avg `0.0325` n `6`; index avg `0.0408` n `25`; metal avg `-0.1648` n `20`; unknown avg `0.5366` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
