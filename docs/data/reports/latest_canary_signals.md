# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T10:42:57.330048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0286` n `12`; crypto_alt avg `-0.114` n `229`; crypto_major avg `-0.1266` n `8`; equity avg `-0.0901` n `91`; fx avg `0.0007` n `6`; index avg `-0.0019` n `25`; metal avg `-0.0346` n `20`; unknown avg `0.0119` n `764`
- 1h: commodity avg `0.1456` n `12`; crypto_alt avg `-0.0464` n `229`; crypto_major avg `-0.0887` n `8`; equity avg `-0.0562` n `91`; fx avg `-0.0118` n `6`; index avg `0.0036` n `25`; metal avg `-0.1135` n `20`; unknown avg `0.0401` n `764`
- 4h: commodity avg `0.0256` n `12`; crypto_alt avg `-0.302` n `229`; crypto_major avg `-0.4332` n `8`; equity avg `0.1337` n `91`; fx avg `0.0131` n `6`; index avg `0.0035` n `25`; metal avg `0.0392` n `20`; unknown avg `0.0114` n `764`
- 24h: commodity avg `-0.3013` n `12`; crypto_alt avg `1.6556` n `229`; crypto_major avg `0.639` n `8`; equity avg `3.2681` n `91`; fx avg `0.161` n `6`; index avg `0.4982` n `25`; metal avg `0.5799` n `20`; unknown avg `0.7803` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0982`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0701`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0662`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0641`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0623`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0623`, n `669`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `669`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `669`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0543`, n `669`, weak_sample_signal
