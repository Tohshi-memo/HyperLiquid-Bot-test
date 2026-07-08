# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T12:22:38.512344+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.083` n `12`; crypto_alt avg `-0.0779` n `229`; crypto_major avg `-0.1537` n `8`; equity avg `-0.112` n `91`; fx avg `-0.0021` n `6`; index avg `-0.0323` n `25`; metal avg `-0.038` n `20`; unknown avg `0.0128` n `757`
- 1h: commodity avg `-0.1772` n `12`; crypto_alt avg `0.5759` n `229`; crypto_major avg `0.432` n `8`; equity avg `0.6402` n `91`; fx avg `-0.0144` n `6`; index avg `0.1295` n `25`; metal avg `0.1754` n `20`; unknown avg `0.3249` n `757`
- 4h: commodity avg `-0.1317` n `12`; crypto_alt avg `0.2658` n `229`; crypto_major avg `0.3136` n `8`; equity avg `-0.4016` n `91`; fx avg `-0.0077` n `6`; index avg `-0.0581` n `25`; metal avg `-0.5334` n `20`; unknown avg `0.1352` n `757`
- 24h: commodity avg `1.3292` n `12`; crypto_alt avg `-3.6783` n `229`; crypto_major avg `-3.2899` n `8`; equity avg `-2.4837` n `91`; fx avg `-0.0716` n `6`; index avg `-0.5826` n `25`; metal avg `-1.4393` n `20`; unknown avg `-0.5167` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
