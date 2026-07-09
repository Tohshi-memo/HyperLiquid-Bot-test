# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T08:07:48.420339+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1072` n `12`; crypto_alt avg `0.1634` n `229`; crypto_major avg `0.108` n `8`; equity avg `0.2561` n `91`; fx avg `0.0314` n `6`; index avg `0.0338` n `25`; metal avg `0.049` n `20`; unknown avg `0.1119` n `764`
- 1h: commodity avg `-0.257` n `12`; crypto_alt avg `-0.0757` n `229`; crypto_major avg `-0.1124` n `8`; equity avg `0.3744` n `91`; fx avg `0.0295` n `6`; index avg `0.0617` n `25`; metal avg `0.1437` n `20`; unknown avg `-0.1005` n `764`
- 4h: commodity avg `-0.4268` n `12`; crypto_alt avg `0.9932` n `229`; crypto_major avg `0.8875` n `8`; equity avg `0.9623` n `91`; fx avg `0.1128` n `6`; index avg `0.147` n `25`; metal avg `0.6636` n `20`; unknown avg `0.1548` n `748`
- 24h: commodity avg `-0.1557` n `12`; crypto_alt avg `0.816` n `229`; crypto_major avg `0.1908` n `8`; equity avg `1.9923` n `91`; fx avg `0.17` n `6`; index avg `0.2433` n `25`; metal avg `-0.2844` n `20`; unknown avg `0.3393` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1012`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0996`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0711`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0676`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0675`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0652`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0594`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.059`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0579`, n `669`, weak_sample_signal
