# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T18:52:41.725820+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `12`; crypto_alt avg `-0.0468` n `230`; crypto_major avg `-0.008` n `8`; equity avg `-0.0817` n `120`; fx avg `-0.0108` n `6`; index avg `-0.0182` n `25`; metal avg `-0.0131` n `20`; unknown avg `0.1296` n `789`
- 1h: commodity avg `0.0383` n `12`; crypto_alt avg `0.003` n `230`; crypto_major avg `0.1713` n `8`; equity avg `-0.0411` n `120`; fx avg `0.0017` n `6`; index avg `-0.0059` n `25`; metal avg `-0.0107` n `20`; unknown avg `0.0186` n `789`
- 4h: commodity avg `0.1657` n `12`; crypto_alt avg `0.0233` n `230`; crypto_major avg `0.1121` n `8`; equity avg `-0.3643` n `120`; fx avg `-0.0141` n `6`; index avg `-0.0777` n `25`; metal avg `-0.1679` n `20`; unknown avg `2.9255` n `789`
- 24h: commodity avg `0.3577` n `12`; crypto_alt avg `-0.6103` n `230`; crypto_major avg `0.1817` n `8`; equity avg `-4.5832` n `120`; fx avg `-0.0454` n `6`; index avg `-0.7056` n `25`; metal avg `-0.6394` n `20`; unknown avg `-0.1991` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
