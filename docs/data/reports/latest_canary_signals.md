# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T21:22:29.086957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `12`; crypto_alt avg `-0.0736` n `229`; crypto_major avg `-0.0414` n `8`; equity avg `-0.0211` n `91`; fx avg `0.0045` n `6`; index avg `-0.0` n `25`; metal avg `-0.0044` n `20`; unknown avg `0.028` n `765`
- 1h: commodity avg `0.0487` n `12`; crypto_alt avg `0.0491` n `229`; crypto_major avg `0.13` n `8`; equity avg `0.0664` n `91`; fx avg `0.0218` n `6`; index avg `-0.0013` n `25`; metal avg `0.0223` n `20`; unknown avg `0.0445` n `765`
- 4h: commodity avg `0.0393` n `12`; crypto_alt avg `0.312` n `229`; crypto_major avg `0.3516` n `8`; equity avg `-0.376` n `91`; fx avg `-0.0246` n `6`; index avg `-0.0129` n `25`; metal avg `-0.222` n `20`; unknown avg `0.0189` n `765`
- 24h: commodity avg `-1.1967` n `12`; crypto_alt avg `1.7362` n `229`; crypto_major avg `1.1772` n `8`; equity avg `1.78` n `91`; fx avg `0.0544` n `6`; index avg `0.3768` n `25`; metal avg `0.6734` n `20`; unknown avg `0.0495` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
