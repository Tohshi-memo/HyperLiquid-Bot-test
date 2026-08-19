# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T11:11:48.265638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0343` n `12`; crypto_alt avg `0.2015` n `230`; crypto_major avg `0.1843` n `8`; equity avg `0.1564` n `120`; fx avg `0.0074` n `6`; index avg `0.0155` n `25`; metal avg `0.03` n `20`; unknown avg `0.1991` n `791`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `0.3474` n `230`; crypto_major avg `0.2792` n `8`; equity avg `0.3352` n `120`; fx avg `-0.0011` n `6`; index avg `0.0554` n `25`; metal avg `0.0713` n `20`; unknown avg `0.176` n `791`
- 4h: commodity avg `0.0271` n `12`; crypto_alt avg `0.3004` n `230`; crypto_major avg `0.3585` n `8`; equity avg `0.3152` n `120`; fx avg `-0.0672` n `6`; index avg `0.062` n `25`; metal avg `0.1528` n `20`; unknown avg `0.119` n `789`
- 24h: commodity avg `0.4516` n `12`; crypto_alt avg `0.3651` n `230`; crypto_major avg `0.4078` n `8`; equity avg `-1.8842` n `120`; fx avg `-0.1947` n `6`; index avg `-0.2213` n `25`; metal avg `-0.4116` n `20`; unknown avg `-0.1281` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
