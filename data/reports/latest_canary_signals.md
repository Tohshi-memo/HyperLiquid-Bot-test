# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T05:22:33.794035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `13`; crypto_alt avg `-0.0533` n `235`; crypto_major avg `-0.0015` n `8`; equity avg `-0.0048` n `143`; fx avg `-0.0006` n `6`; index avg `0.0032` n `26`; metal avg `0.0012` n `20`; unknown avg `0.1736` n `1079`
- 1h: commodity avg `0.0263` n `13`; crypto_alt avg `0.0528` n `235`; crypto_major avg `0.0658` n `8`; equity avg `0.0411` n `143`; fx avg `0.0004` n `6`; index avg `0.0069` n `26`; metal avg `0.0022` n `20`; unknown avg `0.0518` n `1077`
- 4h: commodity avg `-0.0332` n `13`; crypto_alt avg `0.4769` n `235`; crypto_major avg `0.2109` n `8`; equity avg `0.0908` n `143`; fx avg `-0.0001` n `6`; index avg `0.004` n `26`; metal avg `0.0072` n `20`; unknown avg `0.0794` n `1071`
- 24h: commodity avg `0.1943` n `13`; crypto_alt avg `1.6062` n `235`; crypto_major avg `0.7678` n `8`; equity avg `0.2751` n `143`; fx avg `-0.0178` n `6`; index avg `0.0205` n `26`; metal avg `-0.0029` n `20`; unknown avg `0.3645` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1945`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1792`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
