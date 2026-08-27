# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T05:22:32.976370+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0233` n `12`; crypto_alt avg `-0.1282` n `231`; crypto_major avg `0.0451` n `8`; equity avg `-0.0965` n `127`; fx avg `-0.0059` n `6`; index avg `-0.0278` n `26`; metal avg `0.0213` n `20`; unknown avg `-0.0643` n `791`
- 1h: commodity avg `-0.0435` n `12`; crypto_alt avg `-0.4475` n `231`; crypto_major avg `-0.1577` n `8`; equity avg `-0.2564` n `127`; fx avg `0.0004` n `6`; index avg `-0.071` n `26`; metal avg `-0.0075` n `20`; unknown avg `-0.1399` n `791`
- 4h: commodity avg `-0.0735` n `12`; crypto_alt avg `-0.5985` n `231`; crypto_major avg `-0.1882` n `8`; equity avg `0.0628` n `127`; fx avg `0.0285` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0406` n `20`; unknown avg `-0.3684` n `791`
- 24h: commodity avg `0.3584` n `12`; crypto_alt avg `0.0746` n `231`; crypto_major avg `0.4658` n `8`; equity avg `1.065` n `127`; fx avg `-0.0874` n `6`; index avg `0.2019` n `26`; metal avg `-0.2572` n `20`; unknown avg `0.3396` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
