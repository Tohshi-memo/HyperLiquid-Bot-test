# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T02:52:32.360361+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0132` n `13`; crypto_alt avg `0.0954` n `237`; crypto_major avg `0.0602` n `8`; equity avg `-0.0309` n `151`; fx avg `-0.0025` n `6`; index avg `0.0044` n `26`; metal avg `0.011` n `20`; unknown avg `-0.0583` n `1200`
- 1h: commodity avg `0.0316` n `13`; crypto_alt avg `-0.247` n `237`; crypto_major avg `-0.3581` n `8`; equity avg `-0.2785` n `151`; fx avg `0.0015` n `6`; index avg `-0.0287` n `26`; metal avg `-0.0539` n `20`; unknown avg `-0.0671` n `1197`
- 4h: commodity avg `0.1756` n `13`; crypto_alt avg `0.2803` n `237`; crypto_major avg `-0.1089` n `8`; equity avg `0.1161` n `151`; fx avg `0.021` n `6`; index avg `0.0306` n `26`; metal avg `-0.1311` n `20`; unknown avg `-0.0415` n `1159`
- 24h: commodity avg `0.0824` n `13`; crypto_alt avg `2.6635` n `237`; crypto_major avg `1.8591` n `8`; equity avg `1.928` n `151`; fx avg `0.0313` n `6`; index avg `0.2831` n `26`; metal avg `-0.0893` n `20`; unknown avg `211.8749` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1672`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
