# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T21:56:30.779525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `12`; crypto_alt avg `-0.0411` n `230`; crypto_major avg `-0.0121` n `8`; equity avg `-0.0285` n `120`; fx avg `-0.0043` n `6`; index avg `-0.0087` n `25`; metal avg `-0.0133` n `20`; unknown avg `-0.0197` n `789`
- 1h: commodity avg `-0.0378` n `12`; crypto_alt avg `-0.0466` n `230`; crypto_major avg `-0.0509` n `8`; equity avg `-0.108` n `120`; fx avg `0.0012` n `6`; index avg `-0.0001` n `25`; metal avg `0.03` n `20`; unknown avg `-0.1499` n `789`
- 4h: commodity avg `0.0914` n `12`; crypto_alt avg `-0.4148` n `230`; crypto_major avg `-0.0646` n `8`; equity avg `-0.3319` n `120`; fx avg `0.0051` n `6`; index avg `-0.043` n `25`; metal avg `-0.1193` n `20`; unknown avg `-0.0446` n `789`
- 24h: commodity avg `0.2763` n `12`; crypto_alt avg `-0.9265` n `230`; crypto_major avg `0.0246` n `8`; equity avg `-4.5355` n `120`; fx avg `-0.0349` n `6`; index avg `-0.7159` n `25`; metal avg `-0.7714` n `20`; unknown avg `-0.2719` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
