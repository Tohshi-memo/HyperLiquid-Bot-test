# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T07:52:27.816689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0622` n `12`; crypto_alt avg `-0.0235` n `232`; crypto_major avg `0.1355` n `8`; equity avg `-0.0125` n `134`; fx avg `0.0114` n `6`; index avg `0.0042` n `26`; metal avg `0.0491` n `20`; unknown avg `1.4766` n `796`
- 1h: commodity avg `-0.1084` n `12`; crypto_alt avg `-0.6123` n `232`; crypto_major avg `-0.4441` n `8`; equity avg `-0.145` n `134`; fx avg `0.0349` n `6`; index avg `-0.0011` n `26`; metal avg `0.0256` n `20`; unknown avg `0.5782` n `794`
- 4h: commodity avg `-0.0809` n `12`; crypto_alt avg `-0.4002` n `232`; crypto_major avg `-0.2847` n `8`; equity avg `0.0432` n `134`; fx avg `-0.0332` n `6`; index avg `0.0725` n `26`; metal avg `0.0779` n `20`; unknown avg `1.588` n `758`
- 24h: commodity avg `-0.0245` n `12`; crypto_alt avg `-0.2565` n `232`; crypto_major avg `-0.7959` n `8`; equity avg `0.383` n `134`; fx avg `-0.0401` n `6`; index avg `0.0559` n `26`; metal avg `-0.0819` n `20`; unknown avg `382.8621` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1942`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
