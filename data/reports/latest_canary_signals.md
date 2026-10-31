# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T16:52:29.414357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `13`; crypto_alt avg `0.0127` n `238`; crypto_major avg `-0.0135` n `8`; equity avg `0.0191` n `156`; fx avg `0.0015` n `6`; index avg `0.0017` n `27`; metal avg `0.0002` n `20`; unknown avg `1.682` n `1262`
- 1h: commodity avg `-0.0293` n `13`; crypto_alt avg `0.0703` n `238`; crypto_major avg `0.0613` n `8`; equity avg `-0.0014` n `156`; fx avg `0.0013` n `6`; index avg `0.0028` n `27`; metal avg `0.0092` n `20`; unknown avg `2.8393` n `1242`
- 4h: commodity avg `-0.1357` n `13`; crypto_alt avg `0.7022` n `238`; crypto_major avg `0.006` n `8`; equity avg `0.0822` n `156`; fx avg `-0.003` n `6`; index avg `0.0015` n `27`; metal avg `0.0297` n `20`; unknown avg `4.8571` n `1236`
- 24h: commodity avg `-0.4371` n `13`; crypto_alt avg `1.4518` n `238`; crypto_major avg `-0.0116` n `8`; equity avg `0.7343` n `156`; fx avg `-0.0072` n `6`; index avg `0.0046` n `27`; metal avg `-0.005` n `20`; unknown avg `1.6228` n `1081`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
