# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T07:53:03.914071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1123` n `12`; crypto_alt avg `-0.0758` n `230`; crypto_major avg `-0.0696` n `8`; equity avg `-0.1041` n `102`; fx avg `0.0053` n `6`; index avg `0.0117` n `25`; metal avg `0.0558` n `20`; unknown avg `-0.0171` n `784`
- 1h: commodity avg `0.111` n `12`; crypto_alt avg `-0.1687` n `230`; crypto_major avg `-0.1914` n `8`; equity avg `-0.2017` n `102`; fx avg `-0.0345` n `6`; index avg `0.0105` n `25`; metal avg `-0.0002` n `20`; unknown avg `-0.0445` n `784`
- 4h: commodity avg `-0.0705` n `12`; crypto_alt avg `-0.2348` n `230`; crypto_major avg `-0.4523` n `8`; equity avg `-0.5944` n `102`; fx avg `0.0002` n `6`; index avg `-0.0483` n `25`; metal avg `0.0277` n `20`; unknown avg `-0.0059` n `768`
- 24h: commodity avg `-0.2094` n `12`; crypto_alt avg `-1.2393` n `230`; crypto_major avg `-0.9286` n `8`; equity avg `0.3292` n `102`; fx avg `-0.1771` n `6`; index avg `-0.0257` n `25`; metal avg `-0.0547` n `20`; unknown avg `0.9416` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
