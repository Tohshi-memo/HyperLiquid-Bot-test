# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T12:07:28.077376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `0.1715` n `228`; crypto_major avg `-0.0319` n `8`; equity avg `-0.1952` n `74`; fx avg `-0.0027` n `6`; index avg `-0.0558` n `23`; metal avg `-0.1326` n `18`; unknown avg `0.2598` n `643`
- 1h: commodity avg `0.2543` n `12`; crypto_alt avg `-0.0092` n `228`; crypto_major avg `-0.0021` n `8`; equity avg `0.0588` n `74`; fx avg `-0.013` n `6`; index avg `0.0747` n `23`; metal avg `0.0208` n `18`; unknown avg `0.4756` n `643`
- 4h: commodity avg `0.0547` n `12`; crypto_alt avg `0.8707` n `228`; crypto_major avg `0.8018` n `8`; equity avg `0.4642` n `74`; fx avg `0.0026` n `6`; index avg `0.2398` n `23`; metal avg `0.2485` n `18`; unknown avg `1.206` n `643`
- 24h: commodity avg `-2.0962` n `12`; crypto_alt avg `1.784` n `228`; crypto_major avg `1.6837` n `8`; equity avg `2.6172` n `74`; fx avg `0.0034` n `6`; index avg `1.537` n `23`; metal avg `3.1721` n `18`; unknown avg `1.5076` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
