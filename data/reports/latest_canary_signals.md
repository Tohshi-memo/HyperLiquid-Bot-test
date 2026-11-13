# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T20:07:34.411349+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0374` n `13`; crypto_alt avg `0.1415` n `239`; crypto_major avg `0.1758` n `8`; equity avg `0.2164` n `162`; fx avg `-0.0025` n `6`; index avg `0.0294` n `27`; metal avg `0.0298` n `20`; unknown avg `1.5495` n `1246`
- 1h: commodity avg `0.0543` n `13`; crypto_alt avg `0.2718` n `239`; crypto_major avg `0.1352` n `8`; equity avg `0.0179` n `162`; fx avg `-0.0066` n `6`; index avg `0.0125` n `27`; metal avg `-0.0556` n `20`; unknown avg `0.3113` n `1244`
- 4h: commodity avg `-0.1688` n `13`; crypto_alt avg `0.2286` n `239`; crypto_major avg `0.4568` n `8`; equity avg `1.2332` n `162`; fx avg `-0.0521` n `6`; index avg `0.1361` n `27`; metal avg `-0.0993` n `20`; unknown avg `32.0417` n `1244`
- 24h: commodity avg `-0.3745` n `13`; crypto_alt avg `0.3927` n `239`; crypto_major avg `-1.1502` n `8`; equity avg `-2.1525` n `162`; fx avg `-0.0747` n `6`; index avg `-0.1553` n `27`; metal avg `-0.3045` n `20`; unknown avg `1.1862` n `1085`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
