# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T03:07:29.665754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0267` n `13`; crypto_alt avg `-0.174` n `237`; crypto_major avg `-0.0973` n `8`; equity avg `-0.011` n `151`; fx avg `0.0062` n `6`; index avg `0.0121` n `26`; metal avg `-0.0073` n `20`; unknown avg `1.1296` n `1198`
- 1h: commodity avg `0.0239` n `13`; crypto_alt avg `-0.132` n `237`; crypto_major avg `-0.1895` n `8`; equity avg `-0.2129` n `151`; fx avg `0.0028` n `6`; index avg `-0.0096` n `26`; metal avg `-0.041` n `20`; unknown avg `-0.1217` n `1197`
- 4h: commodity avg `0.1822` n `13`; crypto_alt avg `0.3339` n `237`; crypto_major avg `0.0517` n `8`; equity avg `0.2314` n `151`; fx avg `0.0226` n `6`; index avg `0.0748` n `26`; metal avg `-0.1316` n `20`; unknown avg `0.0889` n `1175`
- 24h: commodity avg `0.0557` n `13`; crypto_alt avg `2.4117` n `237`; crypto_major avg `1.676` n `8`; equity avg `1.8511` n `151`; fx avg `0.0392` n `6`; index avg `0.2695` n `26`; metal avg `-0.1607` n `20`; unknown avg `211.9673` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
