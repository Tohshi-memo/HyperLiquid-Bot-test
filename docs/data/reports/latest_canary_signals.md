# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T03:52:13.423840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.1224` n `228`; crypto_major avg `-0.0413` n `8`; equity avg `0.015` n `65`; fx avg `0.0` n `5`; index avg `0.0198` n `23`; metal avg `-0.0033` n `18`; unknown avg `-0.3626` n `375`
- 1h: commodity avg `-0.0573` n `12`; crypto_alt avg `-0.2136` n `228`; crypto_major avg `-0.0198` n `8`; equity avg `-0.0151` n `65`; fx avg `0.0002` n `5`; index avg `-0.0274` n `23`; metal avg `-0.0618` n `18`; unknown avg `-0.7149` n `375`
- 4h: commodity avg `-0.0234` n `12`; crypto_alt avg `0.9532` n `228`; crypto_major avg `0.8229` n `8`; equity avg `0.1494` n `65`; fx avg `-0.0125` n `5`; index avg `0.0915` n `23`; metal avg `0.2681` n `18`; unknown avg `-0.1153` n `375`
- 24h: commodity avg `-0.2544` n `12`; crypto_alt avg `4.178` n `228`; crypto_major avg `2.6906` n `8`; equity avg `3.7988` n `65`; fx avg `0.0723` n `5`; index avg `1.3905` n `23`; metal avg `0.2257` n `18`; unknown avg `1.3377` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
