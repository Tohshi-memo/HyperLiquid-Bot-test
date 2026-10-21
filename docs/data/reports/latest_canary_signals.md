# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T02:37:27.171332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `13`; crypto_alt avg `0.1852` n `237`; crypto_major avg `0.1042` n `8`; equity avg `0.0029` n `151`; fx avg `-0.0004` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0137` n `20`; unknown avg `-0.0132` n `1199`
- 1h: commodity avg `0.0523` n `13`; crypto_alt avg `0.1588` n `237`; crypto_major avg `0.0163` n `8`; equity avg `-0.0672` n `151`; fx avg `0.0027` n `6`; index avg `0.0216` n `26`; metal avg `-0.104` n `20`; unknown avg `0.7561` n `1197`
- 4h: commodity avg `0.1558` n `13`; crypto_alt avg `0.1156` n `237`; crypto_major avg `-0.1818` n `8`; equity avg `0.1237` n `151`; fx avg `0.0175` n `6`; index avg `0.0173` n `26`; metal avg `-0.1636` n `20`; unknown avg `0.2025` n `1159`
- 24h: commodity avg `0.0994` n `13`; crypto_alt avg `3.0005` n `237`; crypto_major avg `2.0912` n `8`; equity avg `2.1787` n `151`; fx avg `0.0483` n `6`; index avg `0.314` n `26`; metal avg `-0.0642` n `20`; unknown avg `211.9641` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
