# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T21:07:38.672664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `13`; crypto_alt avg `0.2651` n `237`; crypto_major avg `0.1219` n `8`; equity avg `0.4434` n `151`; fx avg `-0.0097` n `6`; index avg `0.0345` n `26`; metal avg `0.0208` n `20`; unknown avg `0.8005` n `1191`
- 1h: commodity avg `0.0044` n `13`; crypto_alt avg `0.6062` n `237`; crypto_major avg `0.3515` n `8`; equity avg `1.2032` n `151`; fx avg `-0.0206` n `6`; index avg `0.1373` n `26`; metal avg `0.0485` n `20`; unknown avg `-0.2512` n `1157`
- 4h: commodity avg `0.1321` n `13`; crypto_alt avg `0.1883` n `237`; crypto_major avg `0.2919` n `8`; equity avg `1.0109` n `151`; fx avg `-0.0042` n `6`; index avg `0.1426` n `26`; metal avg `0.0604` n `20`; unknown avg `12.669` n `1127`
- 24h: commodity avg `-0.0453` n `13`; crypto_alt avg `3.2433` n `237`; crypto_major avg `1.9785` n `8`; equity avg `1.199` n `151`; fx avg `0.0016` n `6`; index avg `0.1441` n `26`; metal avg `0.07` n `20`; unknown avg `3.661` n `1034`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
