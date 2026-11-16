# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T13:52:34.927305+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0786` n `13`; crypto_alt avg `0.4501` n `239`; crypto_major avg `0.2745` n `8`; equity avg `0.0327` n `162`; fx avg `-0.0151` n `6`; index avg `0.0014` n `27`; metal avg `-0.0222` n `20`; unknown avg `12.6332` n `1267`
- 1h: commodity avg `-0.071` n `13`; crypto_alt avg `0.4202` n `239`; crypto_major avg `0.34` n `8`; equity avg `-0.1008` n `162`; fx avg `0.0201` n `6`; index avg `-0.0184` n `27`; metal avg `-0.0758` n `20`; unknown avg `13.307` n `1259`
- 4h: commodity avg `-0.2774` n `13`; crypto_alt avg `-0.0853` n `239`; crypto_major avg `-0.023` n `8`; equity avg `-0.6812` n `162`; fx avg `0.0357` n `6`; index avg `-0.0821` n `27`; metal avg `0.095` n `20`; unknown avg `13.228` n `1253`
- 24h: commodity avg `-0.5895` n `13`; crypto_alt avg `-1.901` n `239`; crypto_major avg `-1.9669` n `8`; equity avg `-1.7191` n `162`; fx avg `-0.0289` n `6`; index avg `-0.1429` n `27`; metal avg `-0.0244` n `20`; unknown avg `236.3575` n `1054`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1344`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1153`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1095`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1056`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1039`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1036`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0865`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0851`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0815`, n `669`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0746`, n `669`, weak_sample_signal
