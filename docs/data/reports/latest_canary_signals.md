# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T11:52:28.435727+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `13`; crypto_alt avg `0.0046` n `238`; crypto_major avg `0.0922` n `8`; equity avg `0.0465` n `156`; fx avg `0.0131` n `6`; index avg `0.0016` n `27`; metal avg `0.0031` n `20`; unknown avg `0.1629` n `1260`
- 1h: commodity avg `-0.0011` n `13`; crypto_alt avg `0.197` n `238`; crypto_major avg `0.2594` n `8`; equity avg `0.0523` n `156`; fx avg `-0.0072` n `6`; index avg `0.002` n `27`; metal avg `-0.0008` n `20`; unknown avg `222.1535` n `1230`
- 4h: commodity avg `0.0276` n `13`; crypto_alt avg `0.3307` n `238`; crypto_major avg `0.3355` n `8`; equity avg `0.0529` n `156`; fx avg `0.0005` n `6`; index avg `-0.0095` n `27`; metal avg `0.0369` n `20`; unknown avg `226.433` n `1208`
- 24h: commodity avg `-0.2414` n `13`; crypto_alt avg `0.4465` n `238`; crypto_major avg `-0.4607` n `8`; equity avg `-1.1301` n `156`; fx avg `-0.0459` n `6`; index avg `-0.11` n `27`; metal avg `-0.2267` n `20`; unknown avg `1.6496` n `1039`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
