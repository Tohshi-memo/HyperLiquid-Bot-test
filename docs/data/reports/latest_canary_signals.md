# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T06:52:26.340697+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0343` n `13`; crypto_alt avg `0.037` n `237`; crypto_major avg `0.0012` n `8`; equity avg `0.2282` n `151`; fx avg `0.008` n `6`; index avg `0.052` n `26`; metal avg `0.0682` n `20`; unknown avg `0.0802` n `1198`
- 1h: commodity avg `-0.0303` n `13`; crypto_alt avg `-0.0889` n `237`; crypto_major avg `-0.0738` n `8`; equity avg `0.2718` n `151`; fx avg `0.0217` n `6`; index avg `0.0755` n `26`; metal avg `0.1055` n `20`; unknown avg `2.8547` n `1176`
- 4h: commodity avg `0.0139` n `13`; crypto_alt avg `-0.1624` n `237`; crypto_major avg `-0.163` n `8`; equity avg `-0.5865` n `151`; fx avg `-0.0093` n `6`; index avg `-0.0581` n `26`; metal avg `0.0419` n `20`; unknown avg `0.1087` n `1168`
- 24h: commodity avg `0.3012` n `13`; crypto_alt avg `0.0216` n `237`; crypto_major avg `-0.8063` n `8`; equity avg `-1.3539` n `151`; fx avg `0.0176` n `6`; index avg `-0.1834` n `26`; metal avg `-0.1904` n `20`; unknown avg `5.1003` n `1010`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
