# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T04:37:37.786009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0196` n `13`; crypto_alt avg `0.0639` n `237`; crypto_major avg `0.0691` n `8`; equity avg `0.0258` n `152`; fx avg `0.0027` n `6`; index avg `0.0023` n `26`; metal avg `0.0205` n `20`; unknown avg `0.0136` n `1231`
- 1h: commodity avg `-0.0241` n `13`; crypto_alt avg `0.1762` n `237`; crypto_major avg `0.1752` n `8`; equity avg `0.0467` n `152`; fx avg `0.0073` n `6`; index avg `0.0126` n `26`; metal avg `0.0258` n `20`; unknown avg `1.442` n `1221`
- 4h: commodity avg `-0.0346` n `13`; crypto_alt avg `-0.4152` n `237`; crypto_major avg `0.2953` n `8`; equity avg `0.1201` n `152`; fx avg `0.0076` n `6`; index avg `0.0341` n `26`; metal avg `0.0299` n `20`; unknown avg `-0.114` n `1205`
- 24h: commodity avg `0.2446` n `13`; crypto_alt avg `-1.1998` n `237`; crypto_major avg `0.0409` n `8`; equity avg `0.0153` n `152`; fx avg `-0.0245` n `6`; index avg `0.0091` n `26`; metal avg `-0.0559` n `20`; unknown avg `5.9388` n `1060`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.161`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1564`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
