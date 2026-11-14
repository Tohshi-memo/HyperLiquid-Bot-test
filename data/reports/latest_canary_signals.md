# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T08:22:26.052686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `13`; crypto_alt avg `-0.0279` n `239`; crypto_major avg `-0.0385` n `8`; equity avg `-0.0107` n `162`; fx avg `-0.0001` n `6`; index avg `-0.0008` n `27`; metal avg `-0.0081` n `20`; unknown avg `1.211` n `1260`
- 1h: commodity avg `-0.0026` n `13`; crypto_alt avg `0.3049` n `239`; crypto_major avg `0.2397` n `8`; equity avg `0.0862` n `162`; fx avg `0.0003` n `6`; index avg `0.007` n `27`; metal avg `0.003` n `20`; unknown avg `0.5178` n `1244`
- 4h: commodity avg `0.0457` n `13`; crypto_alt avg `-0.5137` n `239`; crypto_major avg `0.2178` n `8`; equity avg `0.1136` n `162`; fx avg `-0.0029` n `6`; index avg `0.0137` n `27`; metal avg `0.0377` n `20`; unknown avg `1.2966` n `1206`
- 24h: commodity avg `-0.0838` n `13`; crypto_alt avg `-2.3405` n `239`; crypto_major avg `-2.3447` n `8`; equity avg `-2.4043` n `162`; fx avg `-0.1495` n `6`; index avg `-0.1953` n `27`; metal avg `-0.2955` n `20`; unknown avg `58.0209` n `1058`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
