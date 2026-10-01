# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T08:22:38.145304+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0159` n `13`; crypto_alt avg `-0.0136` n `234`; crypto_major avg `-0.0217` n `8`; equity avg `-0.19` n `142`; fx avg `-0.0256` n `6`; index avg `-0.0501` n `26`; metal avg `-0.1269` n `20`; unknown avg `0.292` n `975`
- 1h: commodity avg `0.0515` n `13`; crypto_alt avg `-0.5914` n `234`; crypto_major avg `-0.4286` n `8`; equity avg `-0.4163` n `142`; fx avg `-0.0378` n `6`; index avg `-0.1011` n `26`; metal avg `-0.1729` n `20`; unknown avg `5.1529` n `957`
- 4h: commodity avg `0.7956` n `13`; crypto_alt avg `-0.991` n `234`; crypto_major avg `-0.6402` n `8`; equity avg `-0.4095` n `142`; fx avg `-0.0106` n `6`; index avg `-0.1455` n `26`; metal avg `-0.2986` n `20`; unknown avg `3.4872` n `930`
- 24h: commodity avg `0.1823` n `13`; crypto_alt avg `0.0586` n `234`; crypto_major avg `0.4208` n `8`; equity avg `0.0366` n `142`; fx avg `0.1459` n `6`; index avg `-0.0003` n `26`; metal avg `-0.5321` n `20`; unknown avg `773.0542` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
