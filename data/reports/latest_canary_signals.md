# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T05:37:27.120367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0327` n `13`; crypto_alt avg `0.1062` n `235`; crypto_major avg `0.0421` n `8`; equity avg `0.0416` n `149`; fx avg `-0.0014` n `6`; index avg `0.0099` n `26`; metal avg `0.0072` n `20`; unknown avg `-0.0089` n `1074`
- 1h: commodity avg `0.0195` n `13`; crypto_alt avg `0.2277` n `235`; crypto_major avg `0.0633` n `8`; equity avg `0.0622` n `149`; fx avg `-0.0242` n `6`; index avg `0.0139` n `26`; metal avg `-0.0307` n `20`; unknown avg `4.6386` n `1070`
- 4h: commodity avg `0.0561` n `13`; crypto_alt avg `-0.332` n `235`; crypto_major avg `-0.2748` n `8`; equity avg `0.0542` n `149`; fx avg `-0.0254` n `6`; index avg `0.0011` n `26`; metal avg `-0.1238` n `20`; unknown avg `0.1647` n `1062`
- 24h: commodity avg `-0.0254` n `13`; crypto_alt avg `-0.4154` n `235`; crypto_major avg `0.124` n `8`; equity avg `0.2816` n `149`; fx avg `0.0213` n `6`; index avg `0.1619` n `26`; metal avg `-0.0267` n `20`; unknown avg `587.3193` n `852`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.191`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
