# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T01:52:27.429067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0149` n `12`; crypto_alt avg `-0.3709` n `229`; crypto_major avg `-0.41` n `8`; equity avg `-0.0975` n `91`; fx avg `0.0048` n `6`; index avg `-0.0261` n `25`; metal avg `0.015` n `20`; unknown avg `0.0866` n `764`
- 1h: commodity avg `-0.0013` n `12`; crypto_alt avg `0.1089` n `229`; crypto_major avg `-0.1959` n `8`; equity avg `0.1305` n `91`; fx avg `0.0241` n `6`; index avg `-0.0386` n `25`; metal avg `-0.0051` n `20`; unknown avg `0.0078` n `764`
- 4h: commodity avg `-0.1145` n `12`; crypto_alt avg `0.297` n `229`; crypto_major avg `-0.0487` n `8`; equity avg `0.5442` n `91`; fx avg `0.0239` n `6`; index avg `0.0194` n `25`; metal avg `0.0278` n `20`; unknown avg `-0.1331` n `764`
- 24h: commodity avg `0.3704` n `12`; crypto_alt avg `-0.655` n `229`; crypto_major avg `-1.4097` n `8`; equity avg `1.2947` n `91`; fx avg `0.0502` n `6`; index avg `-0.1243` n `25`; metal avg `-0.694` n `20`; unknown avg `0.0109` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0639`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0531`, n `668`, weak_sample_signal
