# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T04:37:24.829842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0274` n `12`; crypto_alt avg `0.0694` n `230`; crypto_major avg `0.0705` n `8`; equity avg `0.1519` n `102`; fx avg `0.0139` n `6`; index avg `0.0432` n `25`; metal avg `0.0525` n `20`; unknown avg `-0.1785` n `779`
- 1h: commodity avg `-0.0581` n `12`; crypto_alt avg `-0.0973` n `230`; crypto_major avg `-0.0945` n `8`; equity avg `0.4017` n `102`; fx avg `0.0351` n `6`; index avg `0.0535` n `25`; metal avg `0.056` n `20`; unknown avg `-0.0894` n `779`
- 4h: commodity avg `-0.3586` n `12`; crypto_alt avg `-0.4357` n `230`; crypto_major avg `-0.6651` n `8`; equity avg `0.026` n `102`; fx avg `0.1189` n `6`; index avg `-0.014` n `25`; metal avg `-0.1309` n `20`; unknown avg `0.2359` n `779`
- 24h: commodity avg `-0.2359` n `12`; crypto_alt avg `0.0064` n `230`; crypto_major avg `0.7797` n `8`; equity avg `8.6488` n `102`; fx avg `-0.0539` n `6`; index avg `1.1278` n `25`; metal avg `0.6142` n `20`; unknown avg `0.0137` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
