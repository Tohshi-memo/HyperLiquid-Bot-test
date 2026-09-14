# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T11:52:26.855854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `12`; crypto_alt avg `-0.0555` n `233`; crypto_major avg `-0.0863` n `8`; equity avg `-0.1187` n `136`; fx avg `-0.002` n `6`; index avg `-0.0109` n `27`; metal avg `-0.0247` n `20`; unknown avg `0.6638` n `894`
- 1h: commodity avg `0.1315` n `12`; crypto_alt avg `-0.1778` n `233`; crypto_major avg `-0.1286` n `8`; equity avg `-0.2875` n `136`; fx avg `0.011` n `6`; index avg `-0.0152` n `27`; metal avg `-0.013` n `20`; unknown avg `1.0588` n `892`
- 4h: commodity avg `0.0029` n `12`; crypto_alt avg `-0.3133` n `233`; crypto_major avg `-0.0067` n `8`; equity avg `-0.3848` n `136`; fx avg `0.0254` n `6`; index avg `-0.0244` n `27`; metal avg `-0.2311` n `20`; unknown avg `9.2357` n `886`
- 24h: commodity avg `0.591` n `12`; crypto_alt avg `0.0554` n `233`; crypto_major avg `1.6363` n `8`; equity avg `-0.9926` n `136`; fx avg `0.0535` n `6`; index avg `-0.2189` n `27`; metal avg `-0.4671` n `20`; unknown avg `0.9657` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
