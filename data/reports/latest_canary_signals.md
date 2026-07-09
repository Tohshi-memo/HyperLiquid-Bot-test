# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T02:22:25.119966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `12`; crypto_alt avg `0.0764` n `229`; crypto_major avg `0.0546` n `8`; equity avg `0.216` n `91`; fx avg `-0.0138` n `6`; index avg `0.0978` n `25`; metal avg `0.0695` n `20`; unknown avg `-0.0067` n `764`
- 1h: commodity avg `-0.0853` n `12`; crypto_alt avg `-0.3521` n `229`; crypto_major avg `-0.5504` n `8`; equity avg `-0.118` n `91`; fx avg `0.0133` n `6`; index avg `-0.0597` n `25`; metal avg `0.1515` n `20`; unknown avg `-0.0303` n `764`
- 4h: commodity avg `-0.086` n `12`; crypto_alt avg `0.3678` n `229`; crypto_major avg `0.1218` n `8`; equity avg `0.5196` n `91`; fx avg `-0.0219` n `6`; index avg `0.0458` n `25`; metal avg `0.128` n `20`; unknown avg `-0.099` n `764`
- 24h: commodity avg `0.2829` n `12`; crypto_alt avg `0.1255` n `229`; crypto_major avg `-0.5927` n `8`; equity avg `1.2604` n `91`; fx avg `-0.0015` n `6`; index avg `-0.0143` n `25`; metal avg `-0.7029` n `20`; unknown avg `0.1077` n `739`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0527`, n `668`, weak_sample_signal
