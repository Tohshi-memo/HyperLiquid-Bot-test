# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T08:57:15.331124+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1075` n `12`; crypto_alt avg `0.0021` n `229`; crypto_major avg `-0.0359` n `8`; equity avg `-0.1866` n `91`; fx avg `-0.0219` n `6`; index avg `-0.041` n `25`; metal avg `-0.0115` n `20`; unknown avg `-0.0531` n `764`
- 1h: commodity avg `-0.0003` n `12`; crypto_alt avg `0.1652` n `229`; crypto_major avg `0.072` n `8`; equity avg `0.0687` n `91`; fx avg `0.0095` n `6`; index avg `-0.0072` n `25`; metal avg `0.0374` n `20`; unknown avg `0.0738` n `764`
- 4h: commodity avg `-0.3161` n `12`; crypto_alt avg `0.6437` n `229`; crypto_major avg `0.5288` n `8`; equity avg `0.6802` n `91`; fx avg `0.1093` n `6`; index avg `0.1033` n `25`; metal avg `0.63` n `20`; unknown avg `0.1548` n `748`
- 24h: commodity avg `-0.6011` n `12`; crypto_alt avg `1.5954` n `229`; crypto_major avg `0.9191` n `8`; equity avg `3.3692` n `91`; fx avg `0.1041` n `6`; index avg `0.4772` n `25`; metal avg `0.459` n `20`; unknown avg `0.6231` n `741`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1011`, n `670`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0997`, n `670`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0711`, n `670`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0678`, n `670`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0674`, n `670`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0648`, n `670`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0643`, n `670`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0593`, n `670`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0591`, n `670`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0581`, n `670`, weak_sample_signal
