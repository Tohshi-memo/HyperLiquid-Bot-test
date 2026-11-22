# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T03:07:35.358688+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `13`; crypto_alt avg `-0.2328` n `239`; crypto_major avg `-0.3088` n `8`; equity avg `-0.0568` n `166`; fx avg `0.0062` n `6`; index avg `-0.0165` n `27`; metal avg `-0.0198` n `20`; unknown avg `0.8641` n `1255`
- 1h: commodity avg `-0.0475` n `13`; crypto_alt avg `-0.954` n `239`; crypto_major avg `-1.0902` n `8`; equity avg `-0.3621` n `166`; fx avg `0.009` n `6`; index avg `-0.0986` n `27`; metal avg `-0.0897` n `20`; unknown avg `283.7654` n `1259`
- 4h: commodity avg `-0.0313` n `13`; crypto_alt avg `-0.9694` n `239`; crypto_major avg `-0.9833` n `8`; equity avg `-0.2602` n `166`; fx avg `-0.0138` n `6`; index avg `-0.0542` n `27`; metal avg `-0.0779` n `20`; unknown avg `41.7906` n `1254`
- 24h: commodity avg `-0.0229` n `13`; crypto_alt avg `0.436` n `239`; crypto_major avg `2.095` n `8`; equity avg `0.5239` n `166`; fx avg `-0.0399` n `6`; index avg `0.1019` n `27`; metal avg `0.0661` n `20`; unknown avg `233.9194` n `1078`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
