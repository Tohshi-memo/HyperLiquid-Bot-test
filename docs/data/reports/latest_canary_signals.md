# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T14:22:28.103853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `12`; crypto_alt avg `-0.1865` n `230`; crypto_major avg `-0.2029` n `8`; equity avg `0.149` n `96`; fx avg `0.005` n `6`; index avg `0.0204` n `25`; metal avg `0.036` n `20`; unknown avg `-0.0165` n `769`
- 1h: commodity avg `-0.0195` n `12`; crypto_alt avg `0.7651` n `230`; crypto_major avg `0.6012` n `8`; equity avg `1.7952` n `96`; fx avg `0.009` n `6`; index avg `0.2305` n `25`; metal avg `0.2765` n `20`; unknown avg `0.1358` n `769`
- 4h: commodity avg `0.278` n `12`; crypto_alt avg `-0.183` n `230`; crypto_major avg `-0.2332` n `8`; equity avg `0.786` n `96`; fx avg `-0.0046` n `6`; index avg `0.091` n `25`; metal avg `-0.0009` n `20`; unknown avg `0.1922` n `769`
- 24h: commodity avg `0.1031` n `12`; crypto_alt avg `-2.0628` n `230`; crypto_major avg `-3.0671` n `8`; equity avg `-2.6742` n `94`; fx avg `-0.0514` n `6`; index avg `-0.4765` n `25`; metal avg `-0.3695` n `20`; unknown avg `-0.345` n `736`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
