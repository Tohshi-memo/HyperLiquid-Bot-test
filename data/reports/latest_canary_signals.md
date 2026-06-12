# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T06:21:37.695276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1549` n `12`; crypto_alt avg `-0.3355` n `228`; crypto_major avg `-0.4091` n `8`; equity avg `-0.0986` n `74`; fx avg `-0.0005` n `6`; index avg `0.0205` n `23`; metal avg `0.0711` n `18`; unknown avg `-0.074` n `557`
- 1h: commodity avg `0.0295` n `12`; crypto_alt avg `-0.6282` n `228`; crypto_major avg `-0.6517` n `8`; equity avg `-0.6593` n `74`; fx avg `-0.0075` n `6`; index avg `-0.3241` n `23`; metal avg `-0.0737` n `18`; unknown avg `-0.5308` n `535`
- 4h: commodity avg `-0.0511` n `12`; crypto_alt avg `-0.7907` n `228`; crypto_major avg `-0.8018` n `8`; equity avg `-0.6267` n `74`; fx avg `0.0076` n `6`; index avg `-0.2469` n `23`; metal avg `-0.217` n `18`; unknown avg `0.9858` n `535`
- 24h: commodity avg `-2.1914` n `12`; crypto_alt avg `0.8563` n `228`; crypto_major avg `1.0602` n `8`; equity avg `2.8187` n `74`; fx avg `-0.0243` n `6`; index avg `1.543` n `23`; metal avg `2.7249` n `18`; unknown avg `1.5221` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
