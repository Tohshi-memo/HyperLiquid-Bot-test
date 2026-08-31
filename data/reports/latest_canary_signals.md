# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T10:37:29.292862+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0386` n `12`; crypto_alt avg `0.2077` n `232`; crypto_major avg `0.2032` n `8`; equity avg `0.0293` n `128`; fx avg `-0.0138` n `6`; index avg `-0.0026` n `26`; metal avg `0.0162` n `20`; unknown avg `0.0254` n `794`
- 1h: commodity avg `0.0914` n `12`; crypto_alt avg `0.023` n `232`; crypto_major avg `0.054` n `8`; equity avg `-0.1438` n `128`; fx avg `0.0032` n `6`; index avg `-0.0413` n `26`; metal avg `0.0099` n `20`; unknown avg `0.0358` n `792`
- 4h: commodity avg `0.2141` n `12`; crypto_alt avg `-0.0094` n `232`; crypto_major avg `0.422` n `8`; equity avg `-0.2576` n `128`; fx avg `-0.0327` n `6`; index avg `-0.0367` n `26`; metal avg `0.0149` n `20`; unknown avg `0.3622` n `791`
- 24h: commodity avg `0.6625` n `12`; crypto_alt avg `-0.4137` n `231`; crypto_major avg `-0.9473` n `8`; equity avg `-0.4423` n `128`; fx avg `-0.1235` n `6`; index avg `-0.0896` n `26`; metal avg `-0.2212` n `20`; unknown avg `-0.1286` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0486`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0449`, n `668`, weak_sample_signal
