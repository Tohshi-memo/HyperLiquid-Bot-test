# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T12:56:40.044319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0983` n `12`; crypto_alt avg `-0.1453` n `229`; crypto_major avg `-0.2137` n `8`; equity avg `-0.0225` n `91`; fx avg `-0.0177` n `6`; index avg `-0.0154` n `25`; metal avg `-0.0506` n `20`; unknown avg `0.0399` n `765`
- 1h: commodity avg `0.0005` n `12`; crypto_alt avg `0.0254` n `229`; crypto_major avg `-0.0536` n `8`; equity avg `0.2231` n `91`; fx avg `-0.0071` n `6`; index avg `0.0556` n `25`; metal avg `0.118` n `20`; unknown avg `0.0236` n `764`
- 4h: commodity avg `0.2072` n `12`; crypto_alt avg `-0.1912` n `229`; crypto_major avg `-0.5351` n `8`; equity avg `0.4104` n `91`; fx avg `-0.0212` n `6`; index avg `0.1406` n `25`; metal avg `0.111` n `20`; unknown avg `0.0864` n `764`
- 24h: commodity avg `-0.0853` n `12`; crypto_alt avg `1.3435` n `229`; crypto_major avg `0.2583` n `8`; equity avg `3.0001` n `91`; fx avg `0.1307` n `6`; index avg `0.4422` n `25`; metal avg `0.5426` n `20`; unknown avg `0.6764` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0993`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0978`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0753`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0685`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0664`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0607`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0599`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0591`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0583`, n `669`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0576`, n `669`, weak_sample_signal
