# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T11:52:34.626502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.086` n `12`; crypto_alt avg `-0.12` n `228`; crypto_major avg `-0.0168` n `8`; equity avg `0.2144` n `86`; fx avg `0.0093` n `6`; index avg `0.0525` n `23`; metal avg `0.008` n `20`; unknown avg `-0.0315` n `764`
- 1h: commodity avg `-0.1106` n `12`; crypto_alt avg `0.5578` n `228`; crypto_major avg `0.4827` n `8`; equity avg `0.6306` n `86`; fx avg `-0.0054` n `6`; index avg `0.0819` n `23`; metal avg `-0.1088` n `20`; unknown avg `0.2713` n `764`
- 4h: commodity avg `-0.0258` n `12`; crypto_alt avg `-0.558` n `228`; crypto_major avg `-0.9458` n `8`; equity avg `0.3332` n `86`; fx avg `-0.0575` n `6`; index avg `0.0019` n `23`; metal avg `0.1146` n `20`; unknown avg `-0.631` n `764`
- 24h: commodity avg `-0.6138` n `12`; crypto_alt avg `-4.3025` n `228`; crypto_major avg `-4.4693` n `8`; equity avg `-4.0856` n `85`; fx avg `-0.1251` n `6`; index avg `-0.877` n `23`; metal avg `-1.3031` n `20`; unknown avg `0.0807` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1519`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
