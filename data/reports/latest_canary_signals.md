# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T08:07:31.832655+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0079` n `13`; crypto_alt avg `-0.126` n `235`; crypto_major avg `0.0178` n `8`; equity avg `0.0944` n `151`; fx avg `-0.0069` n `6`; index avg `-0.0163` n `26`; metal avg `-0.004` n `20`; unknown avg `0.1947` n `1117`
- 1h: commodity avg `-0.0791` n `13`; crypto_alt avg `0.0336` n `235`; crypto_major avg `0.3497` n `8`; equity avg `0.3663` n `151`; fx avg `0.0244` n `6`; index avg `0.0425` n `26`; metal avg `0.0285` n `20`; unknown avg `0.3834` n `1117`
- 4h: commodity avg `-0.0034` n `13`; crypto_alt avg `0.7963` n `235`; crypto_major avg `0.685` n `8`; equity avg `0.1175` n `151`; fx avg `0.0313` n `6`; index avg `0.0835` n `26`; metal avg `0.0519` n `20`; unknown avg `0.6183` n `1097`
- 24h: commodity avg `0.3646` n `13`; crypto_alt avg `-3.562` n `235`; crypto_major avg `-1.9285` n `8`; equity avg `-3.2849` n `151`; fx avg `0.0857` n `6`; index avg `-0.4489` n `26`; metal avg `0.0041` n `20`; unknown avg `0.5425` n `883`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.193`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1733`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1544`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1334`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.087`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0783`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0782`, n `666`, weak_sample_signal
