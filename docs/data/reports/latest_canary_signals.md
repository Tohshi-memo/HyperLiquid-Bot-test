# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T18:42:08.438181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0295` n `12`; crypto_alt avg `0.0752` n `230`; crypto_major avg `0.206` n `8`; equity avg `0.0358` n `92`; fx avg `0.0022` n `6`; index avg `-0.0421` n `25`; metal avg `-0.0052` n `20`; unknown avg `-0.0109` n `765`
- 1h: commodity avg `0.0317` n `12`; crypto_alt avg `-0.1538` n `230`; crypto_major avg `-0.0193` n `8`; equity avg `0.0024` n `92`; fx avg `-0.0169` n `6`; index avg `-0.0325` n `25`; metal avg `0.0009` n `20`; unknown avg `-0.0111` n `765`
- 4h: commodity avg `0.1458` n `12`; crypto_alt avg `0.0968` n `230`; crypto_major avg `0.3746` n `8`; equity avg `0.0061` n `92`; fx avg `-0.027` n `6`; index avg `0.0015` n `25`; metal avg `-0.0087` n `20`; unknown avg `-0.0752` n `759`
- 24h: commodity avg `0.5647` n `12`; crypto_alt avg `-1.502` n `230`; crypto_major avg `-0.6061` n `8`; equity avg `-0.2162` n `92`; fx avg `-0.0034` n `6`; index avg `-0.1209` n `25`; metal avg `-0.105` n `20`; unknown avg `0.1414` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
