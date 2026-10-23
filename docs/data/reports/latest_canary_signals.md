# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T07:22:28.813973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `13`; crypto_alt avg `0.062` n `237`; crypto_major avg `-0.059` n `8`; equity avg `0.0135` n `152`; fx avg `-0.0284` n `6`; index avg `-0.0046` n `26`; metal avg `-0.0276` n `20`; unknown avg `0.0604` n `1233`
- 1h: commodity avg `-0.0218` n `13`; crypto_alt avg `-0.1254` n `237`; crypto_major avg `-0.128` n `8`; equity avg `-0.0236` n `152`; fx avg `-0.0274` n `6`; index avg `-0.0483` n `26`; metal avg `-0.129` n `20`; unknown avg `-0.034` n `1231`
- 4h: commodity avg `0.0164` n `13`; crypto_alt avg `0.4963` n `237`; crypto_major avg `0.3325` n `8`; equity avg `1.4756` n `152`; fx avg `-0.0279` n `6`; index avg `0.1272` n `26`; metal avg `-0.0339` n `20`; unknown avg `-0.1752` n `1204`
- 24h: commodity avg `0.1917` n `13`; crypto_alt avg `-0.2875` n `237`; crypto_major avg `-0.2206` n `8`; equity avg `-1.0591` n `152`; fx avg `-0.0834` n `6`; index avg `-0.0908` n `26`; metal avg `-0.5286` n `20`; unknown avg `52.0535` n `898`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1785`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
