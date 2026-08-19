# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T11:22:28.513540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0247` n `12`; crypto_alt avg `0.0146` n `230`; crypto_major avg `-0.027` n `8`; equity avg `-0.0651` n `120`; fx avg `0.0023` n `6`; index avg `-0.0044` n `25`; metal avg `0.0048` n `20`; unknown avg `-0.0517` n `792`
- 1h: commodity avg `-0.0068` n `12`; crypto_alt avg `0.3448` n `230`; crypto_major avg `0.22` n `8`; equity avg `0.2769` n `120`; fx avg `0.015` n `6`; index avg `0.0315` n `25`; metal avg `0.0285` n `20`; unknown avg `0.2687` n `791`
- 4h: commodity avg `0.0305` n `12`; crypto_alt avg `0.3015` n `230`; crypto_major avg `0.273` n `8`; equity avg `-0.0469` n `120`; fx avg `-0.0812` n `6`; index avg `0.0366` n `25`; metal avg `0.1376` n `20`; unknown avg `0.1164` n `789`
- 24h: commodity avg `0.416` n `12`; crypto_alt avg `0.2786` n `230`; crypto_major avg `0.1958` n `8`; equity avg `-1.9473` n `120`; fx avg `-0.1943` n `6`; index avg `-0.2276` n `25`; metal avg `-0.418` n `20`; unknown avg `-0.2489` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
