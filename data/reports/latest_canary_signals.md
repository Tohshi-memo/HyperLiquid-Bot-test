# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T10:52:28.391541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.45` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0243` n `13`; crypto_alt avg `-0.1461` n `237`; crypto_major avg `-0.0787` n `8`; equity avg `-0.0401` n `151`; fx avg `-0.0039` n `6`; index avg `-0.0097` n `26`; metal avg `-0.0454` n `20`; unknown avg `-0.0541` n `1201`
- 1h: commodity avg `-0.0328` n `13`; crypto_alt avg `0.0402` n `237`; crypto_major avg `0.1851` n `8`; equity avg `0.3529` n `151`; fx avg `0.0082` n `6`; index avg `0.0588` n `26`; metal avg `0.0247` n `20`; unknown avg `0.3413` n `1199`
- 4h: commodity avg `0.0017` n `13`; crypto_alt avg `-0.4868` n `237`; crypto_major avg `-0.5078` n `8`; equity avg `-0.1488` n `151`; fx avg `-0.0743` n `6`; index avg `-0.003` n `26`; metal avg `-0.095` n `20`; unknown avg `10.2566` n `1089`
- 24h: commodity avg `-0.3352` n `13`; crypto_alt avg `-2.2442` n `237`; crypto_major avg `-1.7052` n `8`; equity avg `-1.9236` n `151`; fx avg `-0.1664` n `6`; index avg `-0.3031` n `26`; metal avg `-0.5069` n `20`; unknown avg `18.1923` n `898`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1408`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
