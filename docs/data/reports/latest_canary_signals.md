# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T22:22:25.713730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0242` n `13`; crypto_alt avg `-0.1431` n `238`; crypto_major avg `-0.0967` n `8`; equity avg `-0.0236` n `156`; fx avg `0.0036` n `6`; index avg `-0.0054` n `27`; metal avg `0.0012` n `20`; unknown avg `2.5459` n `1252`
- 1h: commodity avg `0.0411` n `13`; crypto_alt avg `0.067` n `238`; crypto_major avg `0.2002` n `8`; equity avg `0.0279` n `156`; fx avg `-0.0005` n `6`; index avg `0.0012` n `27`; metal avg `0.0145` n `20`; unknown avg `6.0593` n `1154`
- 4h: commodity avg `0.028` n `13`; crypto_alt avg `-0.2994` n `238`; crypto_major avg `-0.1202` n `8`; equity avg `-0.0051` n `156`; fx avg `0.002` n `6`; index avg `-0.0105` n `27`; metal avg `0.0149` n `20`; unknown avg `1.2747` n `1112`
- 24h: commodity avg `-0.0277` n `13`; crypto_alt avg `0.0835` n `238`; crypto_major avg `0.3754` n `8`; equity avg `0.2289` n `156`; fx avg `0.0167` n `6`; index avg `-0.0535` n `27`; metal avg `0.0526` n `20`; unknown avg `1.1018` n `1051`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
