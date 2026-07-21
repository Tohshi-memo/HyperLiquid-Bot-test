# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T21:07:28.416782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `0.0113` n `230`; crypto_major avg `-0.0177` n `8`; equity avg `0.1789` n `98`; fx avg `-0.0214` n `6`; index avg `0.0226` n `25`; metal avg `0.0128` n `20`; unknown avg `-0.0374` n `771`
- 1h: commodity avg `-0.0016` n `12`; crypto_alt avg `0.0254` n `230`; crypto_major avg `-0.0336` n `8`; equity avg `0.3759` n `98`; fx avg `-0.0201` n `6`; index avg `0.0128` n `25`; metal avg `-0.0219` n `20`; unknown avg `0.0723` n `771`
- 4h: commodity avg `0.0983` n `12`; crypto_alt avg `0.0022` n `230`; crypto_major avg `-0.3601` n `8`; equity avg `0.3605` n `98`; fx avg `0.0178` n `6`; index avg `-0.0181` n `25`; metal avg `0.0109` n `20`; unknown avg `-0.1451` n `771`
- 24h: commodity avg `0.4889` n `12`; crypto_alt avg `0.6316` n `230`; crypto_major avg `0.4445` n `8`; equity avg `4.4433` n `98`; fx avg `0.0453` n `6`; index avg `0.6527` n `25`; metal avg `0.7287` n `20`; unknown avg `0.282` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0841`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
