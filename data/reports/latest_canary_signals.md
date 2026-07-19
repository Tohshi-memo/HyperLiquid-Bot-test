# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T11:22:29.676404+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0493` n `12`; crypto_alt avg `-0.0188` n `230`; crypto_major avg `0.0991` n `8`; equity avg `0.0213` n `96`; fx avg `0.0045` n `6`; index avg `0.004` n `25`; metal avg `-0.0087` n `20`; unknown avg `0.0` n `770`
- 1h: commodity avg `-0.0544` n `12`; crypto_alt avg `0.1588` n `230`; crypto_major avg `0.2748` n `8`; equity avg `0.0229` n `96`; fx avg `0.0335` n `6`; index avg `0.0077` n `25`; metal avg `-0.008` n `20`; unknown avg `0.0743` n `770`
- 4h: commodity avg `-0.0067` n `12`; crypto_alt avg `0.0771` n `230`; crypto_major avg `0.2462` n `8`; equity avg `0.0632` n `96`; fx avg `0.0034` n `6`; index avg `0.0112` n `25`; metal avg `-0.0576` n `20`; unknown avg `-0.0099` n `770`
- 24h: commodity avg `0.1376` n `12`; crypto_alt avg `0.5387` n `230`; crypto_major avg `1.2616` n `8`; equity avg `0.23` n `96`; fx avg `0.0054` n `6`; index avg `-0.052` n `25`; metal avg `-0.0905` n `20`; unknown avg `0.1412` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1124`, n `667`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1117`, n `667`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1001`, n `667`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `667`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
