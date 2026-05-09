# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T12:22:23.209323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0292` n `12`; crypto_alt avg `-0.1454` n `228`; crypto_major avg `-0.0593` n `8`; equity avg `-0.0309` n `65`; fx avg `0.0` n `5`; index avg `-0.0146` n `23`; metal avg `-0.0095` n `18`; unknown avg `-0.272` n `376`
- 1h: commodity avg `-0.0681` n `12`; crypto_alt avg `-0.0982` n `228`; crypto_major avg `-0.018` n `8`; equity avg `-0.0245` n `65`; fx avg `-0.0134` n `5`; index avg `-0.0223` n `23`; metal avg `0.0277` n `18`; unknown avg `0.0397` n `376`
- 4h: commodity avg `-0.0403` n `12`; crypto_alt avg `-0.5753` n `228`; crypto_major avg `-0.1913` n `8`; equity avg `-0.0549` n `65`; fx avg `-0.0045` n `5`; index avg `-0.0569` n `23`; metal avg `-0.011` n `18`; unknown avg `-0.4946` n `376`
- 24h: commodity avg `-0.1328` n `12`; crypto_alt avg `3.092` n `228`; crypto_major avg `1.9993` n `8`; equity avg `2.7481` n `65`; fx avg `-0.0268` n `5`; index avg `1.0792` n `23`; metal avg `-0.0031` n `18`; unknown avg `0.2364` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
