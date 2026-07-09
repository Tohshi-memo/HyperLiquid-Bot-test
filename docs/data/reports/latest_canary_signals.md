# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T21:07:41.723528+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0526` n `12`; crypto_alt avg `0.0895` n `229`; crypto_major avg `0.149` n `8`; equity avg `0.0402` n `91`; fx avg `0.0197` n `6`; index avg `0.0162` n `25`; metal avg `-0.0016` n `20`; unknown avg `-0.0492` n `765`
- 1h: commodity avg `0.0629` n `12`; crypto_alt avg `0.18` n `229`; crypto_major avg `0.2173` n `8`; equity avg `0.0352` n `91`; fx avg `0.0213` n `6`; index avg `-0.0048` n `25`; metal avg `0.0185` n `20`; unknown avg `-0.0755` n `765`
- 4h: commodity avg `0.0219` n `12`; crypto_alt avg `0.5008` n `229`; crypto_major avg `0.4812` n `8`; equity avg `-0.1845` n `91`; fx avg `-0.0208` n `6`; index avg `0.0284` n `25`; metal avg `-0.2195` n `20`; unknown avg `0.0523` n `765`
- 24h: commodity avg `-1.1772` n `12`; crypto_alt avg `1.7111` n `229`; crypto_major avg `1.0871` n `8`; equity avg `1.8235` n `91`; fx avg `0.0459` n `6`; index avg `0.3739` n `25`; metal avg `0.6716` n `20`; unknown avg `0.0164` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
