# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T21:22:41.960929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `12`; crypto_alt avg `-0.039` n `230`; crypto_major avg `-0.009` n `8`; equity avg `-0.0176` n `120`; fx avg `0.0075` n `6`; index avg `-0.0022` n `25`; metal avg `0.0033` n `20`; unknown avg `-0.1114` n `789`
- 1h: commodity avg `0.0239` n `12`; crypto_alt avg `-0.1378` n `230`; crypto_major avg `-0.0992` n `8`; equity avg `-0.0896` n `120`; fx avg `0.0068` n `6`; index avg `0.0043` n `25`; metal avg `-0.0075` n `20`; unknown avg `0.2862` n `789`
- 4h: commodity avg `0.1098` n `12`; crypto_alt avg `-0.463` n `230`; crypto_major avg `-0.0547` n `8`; equity avg `-0.4441` n `120`; fx avg `0.0153` n `6`; index avg `-0.0565` n `25`; metal avg `-0.1806` n `20`; unknown avg `-0.006` n `789`
- 24h: commodity avg `0.2859` n `12`; crypto_alt avg `-0.8509` n `230`; crypto_major avg `0.11` n `8`; equity avg `-4.4357` n `120`; fx avg `-0.0346` n `6`; index avg `-0.6947` n `25`; metal avg `-0.757` n `20`; unknown avg `-0.2374` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
