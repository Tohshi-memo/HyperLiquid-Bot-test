# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T06:07:37.388448+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `12`; crypto_alt avg `0.0151` n `230`; crypto_major avg `0.0411` n `8`; equity avg `-0.0434` n `102`; fx avg `-0.0308` n `6`; index avg `-0.0086` n `25`; metal avg `0.0596` n `20`; unknown avg `0.0029` n `768`
- 1h: commodity avg `0.034` n `12`; crypto_alt avg `0.2309` n `230`; crypto_major avg `0.1766` n `8`; equity avg `0.0226` n `102`; fx avg `-0.0391` n `6`; index avg `0.0014` n `25`; metal avg `0.0335` n `20`; unknown avg `0.0271` n `768`
- 4h: commodity avg `-0.0477` n `12`; crypto_alt avg `0.009` n `230`; crypto_major avg `-0.134` n `8`; equity avg `-0.1737` n `102`; fx avg `-0.0438` n `6`; index avg `-0.0605` n `25`; metal avg `0.037` n `20`; unknown avg `0.0822` n `768`
- 24h: commodity avg `-0.2435` n `12`; crypto_alt avg `-0.8077` n `230`; crypto_major avg `-0.5013` n `8`; equity avg `0.729` n `102`; fx avg `-0.2656` n `6`; index avg `-0.0155` n `25`; metal avg `-0.0094` n `20`; unknown avg `1.0102` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0662`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
