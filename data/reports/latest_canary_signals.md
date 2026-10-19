# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T23:22:30.194926+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `13`; crypto_alt avg `0.0373` n `237`; crypto_major avg `0.0897` n `8`; equity avg `-0.0683` n `151`; fx avg `0.004` n `6`; index avg `-0.0236` n `26`; metal avg `-0.0103` n `20`; unknown avg `-0.0031` n `1198`
- 1h: commodity avg `0.0159` n `13`; crypto_alt avg `-0.2514` n `237`; crypto_major avg `-0.1501` n `8`; equity avg `-0.0505` n `151`; fx avg `0.0015` n `6`; index avg `-0.0174` n `26`; metal avg `-0.0536` n `20`; unknown avg `0.5751` n `1194`
- 4h: commodity avg `-0.0368` n `13`; crypto_alt avg `0.6974` n `237`; crypto_major avg `0.6177` n `8`; equity avg `-0.0024` n `151`; fx avg `-0.0141` n `6`; index avg `-0.0085` n `26`; metal avg `-0.091` n `20`; unknown avg `4.7448` n `1114`
- 24h: commodity avg `0.0165` n `13`; crypto_alt avg `1.0259` n `237`; crypto_major avg `0.6842` n `8`; equity avg `1.5163` n `151`; fx avg `-0.0147` n `6`; index avg `0.3235` n `26`; metal avg `-0.2048` n `20`; unknown avg `6.0074` n `980`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1922`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
