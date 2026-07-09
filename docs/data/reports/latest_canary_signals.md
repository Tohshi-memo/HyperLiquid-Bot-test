# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T05:52:30.321631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0576` n `12`; crypto_alt avg `0.1986` n `229`; crypto_major avg `0.3345` n `8`; equity avg `0.1987` n `91`; fx avg `0.0186` n `6`; index avg `0.0508` n `25`; metal avg `0.0724` n `20`; unknown avg `3.5629` n `764`
- 1h: commodity avg `-0.1746` n `12`; crypto_alt avg `0.3412` n `229`; crypto_major avg `0.4469` n `8`; equity avg `0.0204` n `91`; fx avg `0.0241` n `6`; index avg `0.0135` n `25`; metal avg `0.2066` n `20`; unknown avg `1.0734` n `764`
- 4h: commodity avg `-0.164` n `12`; crypto_alt avg `0.725` n `229`; crypto_major avg `0.8256` n `8`; equity avg `-0.3811` n `91`; fx avg `-0.0166` n `6`; index avg `-0.0549` n `25`; metal avg `0.1302` n `20`; unknown avg `-0.3822` n `764`
- 24h: commodity avg `0.0316` n `12`; crypto_alt avg `0.4964` n `229`; crypto_major avg `0.1502` n `8`; equity avg `1.1148` n `91`; fx avg `0.0745` n `6`; index avg `0.0801` n `25`; metal avg `-0.8613` n `20`; unknown avg `0.1135` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1001`, n `670`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0908`, n `670`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0753`, n `670`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0722`, n `670`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0639`, n `670`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0613`, n `670`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0612`, n `670`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0591`, n `670`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0586`, n `670`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0555`, n `670`, weak_sample_signal
