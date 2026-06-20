# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T12:22:25.609239+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0037` n `12`; crypto_alt avg `0.0202` n `228`; crypto_major avg `-0.0478` n `8`; equity avg `0.0084` n `78`; fx avg `0.0` n `6`; index avg `0.0057` n `23`; metal avg `-0.0094` n `18`; unknown avg `-0.0818` n `701`
- 1h: commodity avg `-0.0204` n `12`; crypto_alt avg `0.1456` n `228`; crypto_major avg `0.1899` n `8`; equity avg `0.0378` n `78`; fx avg `0.007` n `6`; index avg `0.0039` n `23`; metal avg `-0.0009` n `18`; unknown avg `0.4356` n `573`
- 4h: commodity avg `-0.096` n `12`; crypto_alt avg `0.2185` n `228`; crypto_major avg `0.2907` n `8`; equity avg `-0.134` n `78`; fx avg `0.0316` n `6`; index avg `0.0114` n `23`; metal avg `-0.0033` n `18`; unknown avg `-0.2458` n `573`
- 24h: commodity avg `0.4256` n `12`; crypto_alt avg `-2.9749` n `228`; crypto_major avg `-3.2278` n `8`; equity avg `1.1838` n `78`; fx avg `-0.065` n `6`; index avg `0.2976` n `23`; metal avg `-4.1016` n `18`; unknown avg `-0.116` n `492`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
