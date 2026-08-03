# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T03:52:24.154885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `12`; crypto_alt avg `-0.0759` n `230`; crypto_major avg `-0.0387` n `8`; equity avg `0.1843` n `102`; fx avg `-0.0081` n `6`; index avg `0.0402` n `25`; metal avg `0.0244` n `20`; unknown avg `0.9423` n `784`
- 1h: commodity avg `-0.0373` n `12`; crypto_alt avg `-0.2166` n `230`; crypto_major avg `-0.18` n `8`; equity avg `0.045` n `102`; fx avg `0.0242` n `6`; index avg `0.0161` n `25`; metal avg `-0.0125` n `20`; unknown avg `1.2276` n `784`
- 4h: commodity avg `-0.0715` n `12`; crypto_alt avg `-0.8089` n `230`; crypto_major avg `-0.81` n `8`; equity avg `0.304` n `102`; fx avg `-0.2641` n `6`; index avg `-0.0521` n `25`; metal avg `-0.0702` n `20`; unknown avg `0.3023` n `784`
- 24h: commodity avg `-0.2015` n `12`; crypto_alt avg `-0.6905` n `230`; crypto_major avg `-0.4103` n `8`; equity avg `1.0607` n `102`; fx avg `-0.2379` n `6`; index avg `0.0567` n `25`; metal avg `-0.0448` n `20`; unknown avg `1.288` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
