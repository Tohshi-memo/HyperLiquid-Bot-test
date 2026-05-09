# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T13:22:19.469834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `12`; crypto_alt avg `-0.3883` n `228`; crypto_major avg `-0.1067` n `8`; equity avg `0.0004` n `65`; fx avg `0.0059` n `5`; index avg `-0.0166` n `23`; metal avg `-0.0037` n `18`; unknown avg `-0.1927` n `376`
- 1h: commodity avg `0.0965` n `12`; crypto_alt avg `-0.5949` n `228`; crypto_major avg `-0.2587` n `8`; equity avg `0.0747` n `65`; fx avg `0.0059` n `5`; index avg `0.0361` n `23`; metal avg `-0.0225` n `18`; unknown avg `0.0489` n `376`
- 4h: commodity avg `0.0204` n `12`; crypto_alt avg `-0.513` n `228`; crypto_major avg `-0.2804` n `8`; equity avg `0.1061` n `65`; fx avg `0.0023` n `5`; index avg `-0.0721` n `23`; metal avg `-0.0316` n `18`; unknown avg `-0.3905` n `376`
- 24h: commodity avg `-0.0871` n `12`; crypto_alt avg `2.7287` n `228`; crypto_major avg `2.0953` n `8`; equity avg `2.6969` n `65`; fx avg `0.0149` n `5`; index avg `0.9933` n `23`; metal avg `-0.0717` n `18`; unknown avg `0.4509` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
