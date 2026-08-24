# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T10:37:28.482274+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `0.0723` n `227`; crypto_major avg `0.1004` n `8`; equity avg `0.0633` n `106`; fx avg `-0.0025` n `6`; index avg `0.0059` n `25`; metal avg `0.013` n `20`; unknown avg `1.1047` n `785`
- 1h: commodity avg `-0.024` n `12`; crypto_alt avg `0.2156` n `227`; crypto_major avg `0.3503` n `8`; equity avg `0.0097` n `106`; fx avg `0.0261` n `6`; index avg `0.0003` n `25`; metal avg `0.084` n `20`; unknown avg `0.0462` n `785`
- 4h: commodity avg `0.1329` n `12`; crypto_alt avg `0.4902` n `227`; crypto_major avg `0.3826` n `8`; equity avg `0.1829` n `106`; fx avg `0.0055` n `6`; index avg `0.0396` n `25`; metal avg `-0.077` n `20`; unknown avg `0.437` n `785`
- 24h: commodity avg `-0.2163` n `12`; crypto_alt avg `1.7234` n `227`; crypto_major avg `0.6181` n `8`; equity avg `-1.1726` n `106`; fx avg `-0.1478` n `6`; index avg `-0.1194` n `25`; metal avg `0.1883` n `20`; unknown avg `5.3971` n `769`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
