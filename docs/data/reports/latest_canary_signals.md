# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T04:22:29.612575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0179` n `12`; crypto_alt avg `-0.1855` n `228`; crypto_major avg `-0.1273` n `8`; equity avg `-0.2138` n `88`; fx avg `0.0159` n `6`; index avg `-0.058` n `25`; metal avg `-0.0707` n `20`; unknown avg `0.3889` n `763`
- 1h: commodity avg `0.0607` n `12`; crypto_alt avg `0.3943` n `228`; crypto_major avg `0.6286` n `8`; equity avg `-0.2333` n `88`; fx avg `-0.0168` n `6`; index avg `-0.0894` n `25`; metal avg `0.0412` n `20`; unknown avg `5.4173` n `761`
- 4h: commodity avg `-0.0465` n `12`; crypto_alt avg `1.2497` n `228`; crypto_major avg `1.256` n `8`; equity avg `0.0217` n `88`; fx avg `-0.0223` n `6`; index avg `0.0474` n `25`; metal avg `0.377` n `20`; unknown avg `-0.0774` n `759`
- 24h: commodity avg `-0.6426` n `12`; crypto_alt avg `1.3732` n `228`; crypto_major avg `1.0284` n `8`; equity avg `-1.6245` n `88`; fx avg `-0.0467` n `6`; index avg `-0.4286` n `25`; metal avg `1.1427` n `20`; unknown avg `24.9037` n `735`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
