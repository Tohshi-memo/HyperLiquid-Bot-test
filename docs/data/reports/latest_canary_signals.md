# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T10:22:26.506113+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0448` n `12`; crypto_alt avg `0.0432` n `232`; crypto_major avg `0.0666` n `8`; equity avg `0.0565` n `128`; fx avg `0.0017` n `6`; index avg `0.0078` n `26`; metal avg `-0.0231` n `20`; unknown avg `-0.6187` n `794`
- 1h: commodity avg `0.1169` n `12`; crypto_alt avg `-0.2954` n `232`; crypto_major avg `-0.2553` n `8`; equity avg `-0.2323` n `128`; fx avg `0.0229` n `6`; index avg `-0.0506` n `26`; metal avg `-0.0161` n `20`; unknown avg `-0.029` n `791`
- 4h: commodity avg `0.2326` n `12`; crypto_alt avg `-0.1528` n `232`; crypto_major avg `0.2554` n `8`; equity avg `-0.2944` n `128`; fx avg `0.008` n `6`; index avg `-0.0239` n `26`; metal avg `0.0242` n `20`; unknown avg `0.2681` n `791`
- 24h: commodity avg `0.7033` n `12`; crypto_alt avg `-0.5381` n `231`; crypto_major avg `-1.111` n `8`; equity avg `-0.4722` n `128`; fx avg `-0.1116` n `6`; index avg `-0.0877` n `26`; metal avg `-0.2387` n `20`; unknown avg `-0.0964` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0468`, n `668`, weak_sample_signal
