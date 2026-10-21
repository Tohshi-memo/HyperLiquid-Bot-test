# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T00:22:28.637941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0219` n `13`; crypto_alt avg `0.1428` n `237`; crypto_major avg `0.2268` n `8`; equity avg `0.2644` n `151`; fx avg `-0.0022` n `6`; index avg `0.0743` n `26`; metal avg `0.0151` n `20`; unknown avg `-0.0534` n `1199`
- 1h: commodity avg `0.0371` n `13`; crypto_alt avg `0.2882` n `237`; crypto_major avg `0.268` n `8`; equity avg `0.4507` n `151`; fx avg `-0.0152` n `6`; index avg `0.0682` n `26`; metal avg `0.0432` n `20`; unknown avg `-0.193` n `1191`
- 4h: commodity avg `0.1388` n `13`; crypto_alt avg `0.7821` n `237`; crypto_major avg `0.6166` n `8`; equity avg `1.7334` n `151`; fx avg `-0.0274` n `6`; index avg `0.19` n `26`; metal avg `0.0187` n `20`; unknown avg `1.9478` n `1063`
- 24h: commodity avg `0.0217` n `13`; crypto_alt avg `3.0427` n `237`; crypto_major avg `2.3378` n `8`; equity avg `2.637` n `151`; fx avg `0.0302` n `6`; index avg `0.3495` n `26`; metal avg `0.1591` n `20`; unknown avg `212.0056` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
