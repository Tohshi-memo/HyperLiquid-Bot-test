# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T01:07:25.659612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0384` n `13`; crypto_alt avg `-0.1625` n `239`; crypto_major avg `-0.2538` n `8`; equity avg `-0.3261` n `166`; fx avg `0.0516` n `6`; index avg `-0.0423` n `27`; metal avg `0.0047` n `20`; unknown avg `0.0611` n `1255`
- 1h: commodity avg `0.0338` n `13`; crypto_alt avg `-0.3441` n `239`; crypto_major avg `-0.3895` n `8`; equity avg `-0.3655` n `166`; fx avg `0.0627` n `6`; index avg `-0.0505` n `27`; metal avg `-0.0366` n `20`; unknown avg `-0.2914` n `1255`
- 4h: commodity avg `-0.3503` n `13`; crypto_alt avg `-0.4114` n `239`; crypto_major avg `-0.3201` n `8`; equity avg `0.247` n `166`; fx avg `0.1515` n `6`; index avg `0.0759` n `27`; metal avg `0.2457` n `20`; unknown avg `0.2979` n `1210`
- 24h: commodity avg `-0.4521` n `13`; crypto_alt avg `0.3236` n `239`; crypto_major avg `0.5612` n `8`; equity avg `0.9725` n `166`; fx avg `0.1587` n `6`; index avg `0.1309` n `27`; metal avg `0.2447` n `20`; unknown avg `194.3672` n `1029`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.171`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
