# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T09:37:28.466367+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.7529` n `12`; crypto_alt avg `-0.0245` n `228`; crypto_major avg `-0.1305` n `8`; equity avg `-0.1953` n `74`; fx avg `0.0016` n `6`; index avg `-0.0775` n `23`; metal avg `-0.1906` n `18`; unknown avg `0.0679` n `635`
- 1h: commodity avg `0.0555` n `12`; crypto_alt avg `0.0704` n `228`; crypto_major avg `-0.1848` n `8`; equity avg `-0.1352` n `74`; fx avg `-0.01` n `6`; index avg `-0.0159` n `23`; metal avg `-0.0463` n `18`; unknown avg `0.4246` n `635`
- 4h: commodity avg `-0.0361` n `12`; crypto_alt avg `1.4185` n `228`; crypto_major avg `0.8083` n `8`; equity avg `0.1024` n `74`; fx avg `-0.0421` n `6`; index avg `-0.0312` n `23`; metal avg `0.0689` n `18`; unknown avg `0.577` n `619`
- 24h: commodity avg `0.3771` n `12`; crypto_alt avg `0.5411` n `228`; crypto_major avg `-0.3057` n `8`; equity avg `-0.9874` n `74`; fx avg `0.0117` n `6`; index avg `0.483` n `23`; metal avg `-0.0296` n `18`; unknown avg `31.3365` n `611`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
