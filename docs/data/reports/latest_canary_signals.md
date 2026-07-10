# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T07:07:30.718148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0534` n `12`; crypto_alt avg `-0.0259` n `229`; crypto_major avg `-0.048` n `8`; equity avg `-0.1571` n `91`; fx avg `0.0252` n `6`; index avg `-0.0068` n `25`; metal avg `0.0001` n `20`; unknown avg `0.0029` n `765`
- 1h: commodity avg `-0.0456` n `12`; crypto_alt avg `-0.1854` n `229`; crypto_major avg `-0.2115` n `8`; equity avg `-0.2728` n `91`; fx avg `0.0231` n `6`; index avg `-0.0363` n `25`; metal avg `-0.0286` n `20`; unknown avg `0.9737` n `765`
- 4h: commodity avg `-0.0854` n `12`; crypto_alt avg `-0.2204` n `229`; crypto_major avg `-0.0021` n `8`; equity avg `-0.8575` n `91`; fx avg `-0.0504` n `6`; index avg `-0.1492` n `25`; metal avg `-0.1186` n `20`; unknown avg `1.0249` n `733`
- 24h: commodity avg `-0.9456` n `12`; crypto_alt avg `0.369` n `229`; crypto_major avg `0.6323` n `8`; equity avg `0.4613` n `91`; fx avg `-0.1162` n `6`; index avg `0.2105` n `25`; metal avg `0.3715` n `20`; unknown avg `-0.0813` n `732`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
