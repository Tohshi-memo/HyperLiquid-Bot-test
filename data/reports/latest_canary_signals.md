# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T09:52:27.775445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0187` n `12`; crypto_alt avg `0.0706` n `228`; crypto_major avg `0.0416` n `8`; equity avg `0.0062` n `79`; fx avg `0.0037` n `6`; index avg `-0.0045` n `23`; metal avg `0.0006` n `18`; unknown avg `0.0102` n `701`
- 1h: commodity avg `-0.0146` n `12`; crypto_alt avg `-0.0857` n `228`; crypto_major avg `-0.0092` n `8`; equity avg `0.0907` n `79`; fx avg `0.0349` n `6`; index avg `0.0196` n `23`; metal avg `0.1304` n `18`; unknown avg `-0.0193` n `701`
- 4h: commodity avg `0.096` n `12`; crypto_alt avg `0.2193` n `228`; crypto_major avg `0.3798` n `8`; equity avg `0.4345` n `79`; fx avg `0.0409` n `6`; index avg `0.0681` n `23`; metal avg `0.0787` n `18`; unknown avg `0.2282` n `661`
- 24h: commodity avg `-0.2068` n `12`; crypto_alt avg `-0.3798` n `228`; crypto_major avg `-0.1356` n `8`; equity avg `-0.1615` n `79`; fx avg `0.0492` n `6`; index avg `0.0258` n `23`; metal avg `0.4867` n `18`; unknown avg `0.1098` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
