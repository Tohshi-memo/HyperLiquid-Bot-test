# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T06:37:25.371283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0409` n `12`; crypto_alt avg `0.0104` n `233`; crypto_major avg `-0.068` n `8`; equity avg `-0.0232` n `134`; fx avg `0.0223` n `6`; index avg `0.003` n `26`; metal avg `0.0328` n `20`; unknown avg `0.0381` n `798`
- 1h: commodity avg `0.1019` n `12`; crypto_alt avg `0.3959` n `233`; crypto_major avg `0.3684` n `8`; equity avg `0.202` n `134`; fx avg `0.0111` n `6`; index avg `0.0258` n `26`; metal avg `0.1104` n `20`; unknown avg `0.4918` n `778`
- 4h: commodity avg `-0.0539` n `12`; crypto_alt avg `1.0074` n `233`; crypto_major avg `0.6203` n `8`; equity avg `-0.0814` n `134`; fx avg `-0.081` n `6`; index avg `-0.0285` n `26`; metal avg `0.2488` n `20`; unknown avg `0.5518` n `769`
- 24h: commodity avg `-0.099` n `12`; crypto_alt avg `0.9038` n `232`; crypto_major avg `1.8492` n `8`; equity avg `1.333` n `134`; fx avg `-0.1322` n `6`; index avg `0.0747` n `26`; metal avg `0.0581` n `20`; unknown avg `-0.1611` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
