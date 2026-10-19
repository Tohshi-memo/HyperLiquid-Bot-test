# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T23:57:58.268457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0165` n `13`; crypto_alt avg `-0.1567` n `237`; crypto_major avg `-0.1674` n `8`; equity avg `-0.2319` n `151`; fx avg `-0.0131` n `6`; index avg `-0.0366` n `26`; metal avg `-0.0156` n `20`; unknown avg `0.0114` n `1198`
- 1h: commodity avg `0.0214` n `13`; crypto_alt avg `-0.0118` n `237`; crypto_major avg `-0.0751` n `8`; equity avg `-0.2371` n `151`; fx avg `0.0002` n `6`; index avg `-0.0347` n `26`; metal avg `-0.0238` n `20`; unknown avg `0.4838` n `1195`
- 4h: commodity avg `-0.0378` n `13`; crypto_alt avg `0.8152` n `237`; crypto_major avg `0.6946` n `8`; equity avg `-0.0622` n `151`; fx avg `-0.009` n `6`; index avg `0.0185` n `26`; metal avg `-0.0813` n `20`; unknown avg `4.1944` n `1114`
- 24h: commodity avg `0.125` n `13`; crypto_alt avg `0.5857` n `237`; crypto_major avg `0.3069` n `8`; equity avg `1.0237` n `151`; fx avg `-0.0289` n `6`; index avg `0.2369` n `26`; metal avg `-0.2356` n `20`; unknown avg `4.8692` n `980`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1947`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
