# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T02:37:27.159217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0435` n `12`; crypto_alt avg `-0.2593` n `229`; crypto_major avg `-0.2802` n `8`; equity avg `-0.3203` n `91`; fx avg `0.0035` n `6`; index avg `-0.0881` n `25`; metal avg `-0.0996` n `20`; unknown avg `-0.2249` n `764`
- 1h: commodity avg `0.0558` n `12`; crypto_alt avg `-0.4017` n `229`; crypto_major avg `-0.4745` n `8`; equity avg `-0.4113` n `91`; fx avg `-0.0161` n `6`; index avg `-0.0767` n `25`; metal avg `0.0397` n `20`; unknown avg `-0.1706` n `764`
- 4h: commodity avg `-0.018` n `12`; crypto_alt avg `0.0537` n `229`; crypto_major avg `-0.2265` n `8`; equity avg `0.1614` n `91`; fx avg `0.001` n `6`; index avg `-0.0696` n `25`; metal avg `-0.0006` n `20`; unknown avg `-0.2722` n `764`
- 24h: commodity avg `0.3735` n `12`; crypto_alt avg `-0.0643` n `229`; crypto_major avg `-0.7181` n `8`; equity avg `0.9718` n `91`; fx avg `-0.0003` n `6`; index avg `-0.0797` n `25`; metal avg `-0.8001` n `20`; unknown avg `0.0732` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
