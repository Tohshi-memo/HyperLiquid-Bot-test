# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T02:07:28.301153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0298` n `13`; crypto_alt avg `1.5645` n `239`; crypto_major avg `2.136` n `8`; equity avg `0.3489` n `162`; fx avg `-0.0102` n `6`; index avg `0.0105` n `27`; metal avg `0.052` n `20`; unknown avg `69.1436` n `1255`
- 1h: commodity avg `0.0408` n `13`; crypto_alt avg `0.7559` n `239`; crypto_major avg `1.1991` n `8`; equity avg `0.1978` n `162`; fx avg `-0.001` n `6`; index avg `0.0167` n `27`; metal avg `0.0006` n `20`; unknown avg `70.455` n `1256`
- 4h: commodity avg `0.1567` n `13`; crypto_alt avg `1.4294` n `239`; crypto_major avg `1.0834` n `8`; equity avg `0.1102` n `162`; fx avg `0.0072` n `6`; index avg `-0.0042` n `27`; metal avg `-0.0375` n `20`; unknown avg `1.6564` n `1220`
- 24h: commodity avg `0.0118` n `13`; crypto_alt avg `-7.6802` n `239`; crypto_major avg `-7.5417` n `8`; equity avg `-1.4331` n `162`; fx avg `0.0326` n `6`; index avg `-0.1237` n `27`; metal avg `-0.5651` n `20`; unknown avg `47.3505` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
