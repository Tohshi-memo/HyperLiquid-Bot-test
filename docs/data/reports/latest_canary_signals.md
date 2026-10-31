# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T17:07:26.626067+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `13`; crypto_alt avg `-0.1477` n `238`; crypto_major avg `-0.0936` n `8`; equity avg `-0.0096` n `156`; fx avg `-0.0029` n `6`; index avg `-0.0038` n `27`; metal avg `-0.0014` n `20`; unknown avg `-0.0979` n `1256`
- 1h: commodity avg `-0.0322` n `13`; crypto_alt avg `-0.2142` n `238`; crypto_major avg `-0.1188` n `8`; equity avg `-0.017` n `156`; fx avg `0.0048` n `6`; index avg `0.0073` n `27`; metal avg `0.0081` n `20`; unknown avg `2.2321` n `1256`
- 4h: commodity avg `-0.0826` n `13`; crypto_alt avg `0.8885` n `238`; crypto_major avg `0.0115` n `8`; equity avg `0.1053` n `156`; fx avg `-0.002` n `6`; index avg `-0.0005` n `27`; metal avg `0.0264` n `20`; unknown avg `2.7009` n `1234`
- 24h: commodity avg `-0.4935` n `13`; crypto_alt avg `1.2106` n `238`; crypto_major avg `-0.0938` n `8`; equity avg `0.9017` n `156`; fx avg `-0.0152` n `6`; index avg `0.0036` n `27`; metal avg `0.0232` n `20`; unknown avg `2.234` n `1081`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
