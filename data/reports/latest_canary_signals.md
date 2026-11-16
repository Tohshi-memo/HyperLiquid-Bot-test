# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T07:07:28.695315+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `13`; crypto_alt avg `-0.1225` n `239`; crypto_major avg `-0.0104` n `8`; equity avg `0.0146` n `162`; fx avg `0.0104` n `6`; index avg `0.0144` n `27`; metal avg `0.0598` n `20`; unknown avg `0.1786` n `1183`
- 1h: commodity avg `0.0535` n `13`; crypto_alt avg `0.0228` n `239`; crypto_major avg `0.2751` n `8`; equity avg `0.2698` n `162`; fx avg `0.0035` n `6`; index avg `0.0274` n `27`; metal avg `0.0334` n `20`; unknown avg `0.3542` n `1141`
- 4h: commodity avg `0.272` n `13`; crypto_alt avg `-0.8466` n `239`; crypto_major avg `-0.694` n `8`; equity avg `-1.0199` n `162`; fx avg `-0.0372` n `6`; index avg `-0.0877` n `27`; metal avg `-0.0443` n `20`; unknown avg `0.2779` n `1119`
- 24h: commodity avg `-0.2438` n `13`; crypto_alt avg `-0.0411` n `239`; crypto_major avg `0.8993` n `8`; equity avg `-0.2937` n `162`; fx avg `-0.0621` n `6`; index avg `-0.0112` n `27`; metal avg `0.1135` n `20`; unknown avg `1.1056` n `1079`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
