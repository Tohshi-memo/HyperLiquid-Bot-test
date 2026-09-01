# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T21:07:57.124023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0305` n `12`; crypto_alt avg `0.0127` n `232`; crypto_major avg `-0.127` n `8`; equity avg `0.0038` n `131`; fx avg `-0.0134` n `6`; index avg `0.0045` n `26`; metal avg `0.0227` n `20`; unknown avg `-0.0723` n `785`
- 1h: commodity avg `-0.0368` n `12`; crypto_alt avg `-0.103` n `232`; crypto_major avg `-0.0792` n `8`; equity avg `0.1292` n `131`; fx avg `-0.0078` n `6`; index avg `0.0329` n `26`; metal avg `0.0274` n `20`; unknown avg `0.2788` n `773`
- 4h: commodity avg `0.282` n `12`; crypto_alt avg `-0.1779` n `232`; crypto_major avg `-0.553` n `8`; equity avg `-0.0978` n `131`; fx avg `0.0128` n `6`; index avg `-0.0316` n `26`; metal avg `-0.1833` n `20`; unknown avg `0.4213` n `773`
- 24h: commodity avg `0.8267` n `12`; crypto_alt avg `-0.3343` n `232`; crypto_major avg `-2.1048` n `8`; equity avg `-1.8937` n `130`; fx avg `0.0281` n `6`; index avg `-0.3469` n `26`; metal avg `-0.8652` n `20`; unknown avg `-0.4636` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0449`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0366`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0329`, n `668`, weak_sample_signal
