# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T14:22:27.092779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `13`; crypto_alt avg `0.0354` n `238`; crypto_major avg `-0.0003` n `8`; equity avg `0.0373` n `156`; fx avg `-0.0068` n `6`; index avg `0.0052` n `27`; metal avg `0.0077` n `20`; unknown avg `0.1962` n `1262`
- 1h: commodity avg `-0.0277` n `13`; crypto_alt avg `0.142` n `238`; crypto_major avg `-0.0786` n `8`; equity avg `0.0884` n `156`; fx avg `-0.0068` n `6`; index avg `0.0087` n `27`; metal avg `0.0065` n `20`; unknown avg `1.5879` n `1256`
- 4h: commodity avg `-0.0468` n `13`; crypto_alt avg `0.2786` n `238`; crypto_major avg `-0.0432` n `8`; equity avg `-0.0278` n `156`; fx avg `-0.0211` n `6`; index avg `-0.0135` n `27`; metal avg `0.009` n `20`; unknown avg `15.6333` n `1218`
- 24h: commodity avg `-0.3615` n `13`; crypto_alt avg `1.2345` n `238`; crypto_major avg `0.1019` n `8`; equity avg `-0.3396` n `156`; fx avg `0.0394` n `6`; index avg `-0.0505` n `27`; metal avg `0.0559` n `20`; unknown avg `8.2619` n `1087`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
