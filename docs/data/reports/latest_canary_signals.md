# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T07:07:32.873717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `0.0681` n `234`; crypto_major avg `0.1027` n `8`; equity avg `0.0977` n `140`; fx avg `-0.0011` n `6`; index avg `0.0149` n `26`; metal avg `0.0183` n `20`; unknown avg `0.4613` n `942`
- 1h: commodity avg `-0.0783` n `12`; crypto_alt avg `0.5302` n `234`; crypto_major avg `0.2581` n `8`; equity avg `0.2324` n `140`; fx avg `-0.0432` n `6`; index avg `0.0452` n `26`; metal avg `0.0382` n `20`; unknown avg `0.4811` n `920`
- 4h: commodity avg `0.0231` n `12`; crypto_alt avg `1.0923` n `234`; crypto_major avg `0.4365` n `8`; equity avg `0.1875` n `140`; fx avg `-0.0153` n `6`; index avg `0.0682` n `26`; metal avg `0.0109` n `20`; unknown avg `0.1084` n `890`
- 24h: commodity avg `-0.5786` n `12`; crypto_alt avg `4.1132` n `234`; crypto_major avg `2.887` n `8`; equity avg `1.314` n `140`; fx avg `-0.057` n `6`; index avg `0.2859` n `26`; metal avg `0.0227` n `20`; unknown avg `3.4867` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
