# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T08:52:51.622373+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `12`; crypto_alt avg `-0.0082` n `230`; crypto_major avg `-0.0612` n `8`; equity avg `0.0852` n `113`; fx avg `-0.0248` n `6`; index avg `0.0159` n `25`; metal avg `0.0071` n `20`; unknown avg `0.011` n `787`
- 1h: commodity avg `-0.11` n `12`; crypto_alt avg `-0.0327` n `230`; crypto_major avg `-0.2033` n `8`; equity avg `-0.1911` n `113`; fx avg `-0.0035` n `6`; index avg `-0.0164` n `25`; metal avg `-0.001` n `20`; unknown avg `0.5034` n `787`
- 4h: commodity avg `-0.227` n `12`; crypto_alt avg `0.0805` n `230`; crypto_major avg `0.1273` n `8`; equity avg `-0.6218` n `113`; fx avg `0.0792` n `6`; index avg `-0.0778` n `25`; metal avg `-0.268` n `20`; unknown avg `-0.0011` n `755`
- 24h: commodity avg `-0.3061` n `12`; crypto_alt avg `-0.2505` n `230`; crypto_major avg `0.2194` n `8`; equity avg `1.3774` n `113`; fx avg `0.0169` n `6`; index avg `0.1624` n `25`; metal avg `-0.4881` n `20`; unknown avg `0.7286` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2461`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2137`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1962`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1917`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1724`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
