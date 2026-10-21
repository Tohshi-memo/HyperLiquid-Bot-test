# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T02:07:26.748833+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0344` n `13`; crypto_alt avg `-0.2887` n `237`; crypto_major avg `-0.2661` n `8`; equity avg `-0.0763` n `151`; fx avg `0.005` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0202` n `20`; unknown avg `0.1546` n `1197`
- 1h: commodity avg `0.0546` n `13`; crypto_alt avg `0.4567` n `237`; crypto_major avg `0.2606` n `8`; equity avg `0.3512` n `151`; fx avg `0.0144` n `6`; index avg `0.1361` n `26`; metal avg `0.0383` n `20`; unknown avg `0.4001` n `1197`
- 4h: commodity avg `0.1817` n `13`; crypto_alt avg `0.1222` n `237`; crypto_major avg `-0.0142` n `8`; equity avg `0.3079` n `151`; fx avg `0.002` n `6`; index avg `0.0424` n `26`; metal avg `-0.1235` n `20`; unknown avg `0.2196` n `1119`
- 24h: commodity avg `0.0919` n `13`; crypto_alt avg `3.3491` n `237`; crypto_major avg `2.4242` n `8`; equity avg `2.651` n `151`; fx avg `0.055` n `6`; index avg `0.3652` n `26`; metal avg `0.0078` n `20`; unknown avg `212.0681` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
