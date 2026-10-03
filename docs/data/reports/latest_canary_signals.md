# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T22:22:26.043770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.014` n `13`; crypto_alt avg `0.0279` n `235`; crypto_major avg `-0.0164` n `8`; equity avg `0.0212` n `143`; fx avg `0.0037` n `6`; index avg `0.0028` n `26`; metal avg `0.0038` n `20`; unknown avg `0.0231` n `1079`
- 1h: commodity avg `-0.0026` n `13`; crypto_alt avg `0.0089` n `235`; crypto_major avg `0.0546` n `8`; equity avg `0.0508` n `143`; fx avg `0.0097` n `6`; index avg `0.0084` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.0181` n `1061`
- 4h: commodity avg `0.1029` n `13`; crypto_alt avg `0.3536` n `235`; crypto_major avg `-0.0324` n `8`; equity avg `0.0959` n `143`; fx avg `0.0204` n `6`; index avg `0.0091` n `26`; metal avg `0.0047` n `20`; unknown avg `0.26` n `1046`
- 24h: commodity avg `0.001` n `13`; crypto_alt avg `2.6693` n `235`; crypto_major avg `1.2914` n `8`; equity avg `0.2202` n `143`; fx avg `-0.007` n `6`; index avg `0.049` n `26`; metal avg `-0.0199` n `20`; unknown avg `0.0889` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1993`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
