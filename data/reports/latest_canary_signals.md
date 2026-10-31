# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T13:37:24.794137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `13`; crypto_alt avg `0.0748` n `238`; crypto_major avg `0.0586` n `8`; equity avg `0.0141` n `156`; fx avg `-0.0001` n `6`; index avg `-0.0005` n `27`; metal avg `-0.0046` n `20`; unknown avg `-0.2337` n `1262`
- 1h: commodity avg `-0.0566` n `13`; crypto_alt avg `-0.293` n `238`; crypto_major avg `-0.3076` n `8`; equity avg `-0.0981` n `156`; fx avg `-0.0064` n `6`; index avg `-0.0165` n `27`; metal avg `-0.007` n `20`; unknown avg `0.056` n `1256`
- 4h: commodity avg `-0.0212` n `13`; crypto_alt avg `0.1755` n `238`; crypto_major avg `0.1801` n `8`; equity avg `-0.1164` n `156`; fx avg `-0.0017` n `6`; index avg `-0.0223` n `27`; metal avg `0.0061` n `20`; unknown avg `205.7535` n `1218`
- 24h: commodity avg `-0.1701` n `13`; crypto_alt avg `0.7817` n `238`; crypto_major avg `-0.2262` n `8`; equity avg `-1.2423` n `156`; fx avg `-0.0029` n `6`; index avg `-0.1526` n `27`; metal avg `-0.1435` n `20`; unknown avg `3.6258` n `1045`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
