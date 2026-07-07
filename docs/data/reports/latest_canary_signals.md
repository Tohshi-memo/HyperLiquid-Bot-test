# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T02:07:25.425089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `12`; crypto_alt avg `-0.0869` n `229`; crypto_major avg `-0.2164` n `8`; equity avg `-0.1521` n `91`; fx avg `0.0048` n `6`; index avg `-0.056` n `25`; metal avg `-0.028` n `20`; unknown avg `0.0937` n `763`
- 1h: commodity avg `0.0551` n `12`; crypto_alt avg `-0.1245` n `229`; crypto_major avg `-0.3117` n `8`; equity avg `-0.1431` n `91`; fx avg `-0.0461` n `6`; index avg `-0.0445` n `25`; metal avg `0.129` n `20`; unknown avg `-0.2112` n `761`
- 4h: commodity avg `0.0982` n `12`; crypto_alt avg `-0.8158` n `229`; crypto_major avg `-0.853` n `8`; equity avg `-1.0816` n `91`; fx avg `-0.0497` n `6`; index avg `-0.3173` n `25`; metal avg `-0.1766` n `20`; unknown avg `0.9765` n `761`
- 24h: commodity avg `0.2264` n `12`; crypto_alt avg `0.3718` n `229`; crypto_major avg `-0.3474` n `8`; equity avg `-0.7587` n `90`; fx avg `0.0109` n `6`; index avg `-0.1512` n `25`; metal avg `-0.3249` n `20`; unknown avg `-0.0542` n `727`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
