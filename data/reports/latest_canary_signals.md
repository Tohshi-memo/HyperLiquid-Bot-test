# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T10:07:34.598069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0237` n `12`; crypto_alt avg `-0.0937` n `231`; crypto_major avg `-0.0543` n `8`; equity avg `-0.0351` n `122`; fx avg `-0.005` n `6`; index avg `-0.0055` n `25`; metal avg `-0.0078` n `20`; unknown avg `-0.0058` n `797`
- 1h: commodity avg `0.0583` n `12`; crypto_alt avg `-0.7764` n `231`; crypto_major avg `-0.6281` n `8`; equity avg `-0.0002` n `122`; fx avg `-0.0008` n `6`; index avg `-0.0067` n `25`; metal avg `-0.0207` n `20`; unknown avg `-0.1319` n `797`
- 4h: commodity avg `-0.134` n `12`; crypto_alt avg `-1.059` n `231`; crypto_major avg `-1.0068` n `8`; equity avg `-0.0608` n `122`; fx avg `-0.0141` n `6`; index avg `-0.0233` n `25`; metal avg `-0.1426` n `20`; unknown avg `-0.0268` n `797`
- 24h: commodity avg `-0.3324` n `12`; crypto_alt avg `-2.2137` n `231`; crypto_major avg `-1.9272` n `8`; equity avg `-0.0209` n `122`; fx avg `-0.0381` n `6`; index avg `-0.0694` n `25`; metal avg `0.1468` n `20`; unknown avg `0.6449` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.19`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
