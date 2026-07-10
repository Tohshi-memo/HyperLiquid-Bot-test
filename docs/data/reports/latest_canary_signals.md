# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T01:52:27.105533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `0.6655` n `229`; crypto_major avg `0.8488` n `8`; equity avg `0.0378` n `91`; fx avg `-0.0049` n `6`; index avg `0.0096` n `25`; metal avg `0.0232` n `20`; unknown avg `0.2028` n `765`
- 1h: commodity avg `0.0433` n `12`; crypto_alt avg `1.2621` n `229`; crypto_major avg `1.4561` n `8`; equity avg `0.3959` n `91`; fx avg `0.0125` n `6`; index avg `0.114` n `25`; metal avg `0.0496` n `20`; unknown avg `1.1899` n `765`
- 4h: commodity avg `0.0254` n `12`; crypto_alt avg `0.9487` n `229`; crypto_major avg `1.0974` n `8`; equity avg `0.2418` n `91`; fx avg `0.0301` n `6`; index avg `0.0043` n `25`; metal avg `0.0548` n `20`; unknown avg `0.0388` n `765`
- 24h: commodity avg `-1.006` n `12`; crypto_alt avg `1.9212` n `229`; crypto_major avg `1.9202` n `8`; equity avg `1.2928` n `91`; fx avg `0.044` n `6`; index avg `0.3521` n `25`; metal avg `0.7106` n `20`; unknown avg `-0.0873` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
