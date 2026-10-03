# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T15:52:35.639317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0536` n `13`; crypto_alt avg `0.126` n `235`; crypto_major avg `0.0984` n `8`; equity avg `0.0074` n `143`; fx avg `-0.0112` n `6`; index avg `0.0033` n `26`; metal avg `0.003` n `20`; unknown avg `0.1694` n `1078`
- 1h: commodity avg `0.0859` n `13`; crypto_alt avg `-0.1447` n `235`; crypto_major avg `-0.0488` n `8`; equity avg `0.0283` n `143`; fx avg `-0.0071` n `6`; index avg `0.0097` n `26`; metal avg `0.0016` n `20`; unknown avg `0.0324` n `1020`
- 4h: commodity avg `0.2224` n `13`; crypto_alt avg `0.478` n `235`; crypto_major avg `0.3911` n `8`; equity avg `0.0331` n `143`; fx avg `-0.0195` n `6`; index avg `0.0193` n `26`; metal avg `-0.0132` n `20`; unknown avg `0.0788` n `948`
- 24h: commodity avg `0.6012` n `13`; crypto_alt avg `-1.0426` n `235`; crypto_major avg `-0.5734` n `8`; equity avg `0.0225` n `143`; fx avg `-0.0348` n `6`; index avg `0.0239` n `26`; metal avg `0.1627` n `20`; unknown avg `0.0423` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1969`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
