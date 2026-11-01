# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T07:22:23.694445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `13`; crypto_alt avg `-0.0674` n `238`; crypto_major avg `-0.2384` n `8`; equity avg `-0.0597` n `156`; fx avg `-0.0028` n `6`; index avg `-0.0107` n `27`; metal avg `-0.0122` n `20`; unknown avg `0.2495` n `1263`
- 1h: commodity avg `-0.0294` n `13`; crypto_alt avg `-0.2049` n `238`; crypto_major avg `-0.2181` n `8`; equity avg `-0.0214` n `156`; fx avg `-0.0168` n `6`; index avg `0.0111` n `27`; metal avg `0.014` n `20`; unknown avg `0.4104` n `1255`
- 4h: commodity avg `-0.0038` n `13`; crypto_alt avg `0.2417` n `238`; crypto_major avg `-0.0501` n `8`; equity avg `0.1832` n `156`; fx avg `-0.014` n `6`; index avg `0.025` n `27`; metal avg `0.0165` n `20`; unknown avg `1.3155` n `1228`
- 24h: commodity avg `-0.0567` n `13`; crypto_alt avg `0.4402` n `238`; crypto_major avg `0.1545` n `8`; equity avg `0.2708` n `156`; fx avg `-0.0131` n `6`; index avg `0.0169` n `27`; metal avg `0.0584` n `20`; unknown avg `2.4507` n `996`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
