# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T03:37:27.412112+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0144` n `13`; crypto_alt avg `0.1592` n `237`; crypto_major avg `0.0436` n `8`; equity avg `-0.0739` n `151`; fx avg `-0.0286` n `6`; index avg `-0.0345` n `26`; metal avg `0.0159` n `20`; unknown avg `-0.0081` n `1200`
- 1h: commodity avg `0.02` n `13`; crypto_alt avg `-0.0312` n `237`; crypto_major avg `-0.0747` n `8`; equity avg `-0.0871` n `151`; fx avg `-0.0342` n `6`; index avg `-0.0368` n `26`; metal avg `0.0194` n `20`; unknown avg `0.3636` n `1198`
- 4h: commodity avg `0.1513` n `13`; crypto_alt avg `0.378` n `237`; crypto_major avg `0.1156` n `8`; equity avg `0.2676` n `151`; fx avg `-0.0039` n `6`; index avg `0.015` n `26`; metal avg `-0.081` n `20`; unknown avg `0.4804` n `1191`
- 24h: commodity avg `0.0453` n `13`; crypto_alt avg `2.3559` n `237`; crypto_major avg `1.5996` n `8`; equity avg `2.0016` n `151`; fx avg `0.0085` n `6`; index avg `0.2674` n `26`; metal avg `-0.1465` n `20`; unknown avg `212.8395` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
