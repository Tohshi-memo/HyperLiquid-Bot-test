# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T10:37:28.815865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `13`; crypto_alt avg `-0.088` n `239`; crypto_major avg `0.0495` n `8`; equity avg `-0.0054` n `162`; fx avg `0.0063` n `6`; index avg `-0.0004` n `27`; metal avg `-0.0002` n `20`; unknown avg `76.0741` n `1256`
- 1h: commodity avg `0.0001` n `13`; crypto_alt avg `-0.2574` n `239`; crypto_major avg `0.1277` n `8`; equity avg `-0.0134` n `162`; fx avg `0.0049` n `6`; index avg `0.0016` n `27`; metal avg `0.0016` n `20`; unknown avg `77.9475` n `1240`
- 4h: commodity avg `-0.0208` n `13`; crypto_alt avg `-1.0037` n `239`; crypto_major avg `-0.1318` n `8`; equity avg `0.0304` n `162`; fx avg `-0.009` n `6`; index avg `-0.0007` n `27`; metal avg `0.0309` n `20`; unknown avg `82.2622` n `1168`
- 24h: commodity avg `-0.0409` n `13`; crypto_alt avg `-3.0182` n `239`; crypto_major avg `-3.1964` n `8`; equity avg `-2.7305` n `162`; fx avg `-0.1137` n `6`; index avg `-0.2364` n `27`; metal avg `-0.315` n `20`; unknown avg `1.3335` n `1096`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
