# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T06:07:25.614509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.062` n `12`; crypto_alt avg `-0.0148` n `230`; crypto_major avg `-0.0664` n `8`; equity avg `0.1139` n `98`; fx avg `-0.0003` n `6`; index avg `0.0212` n `25`; metal avg `0.0273` n `20`; unknown avg `-0.0762` n `755`
- 1h: commodity avg `0.0516` n `12`; crypto_alt avg `0.3274` n `230`; crypto_major avg `0.2736` n `8`; equity avg `0.3223` n `98`; fx avg `-0.0032` n `6`; index avg `0.0373` n `25`; metal avg `0.1682` n `20`; unknown avg `0.0162` n `755`
- 4h: commodity avg `0.0384` n `12`; crypto_alt avg `0.8695` n `230`; crypto_major avg `0.6852` n `8`; equity avg `1.5639` n `98`; fx avg `-0.0425` n `6`; index avg `0.1903` n `25`; metal avg `0.4431` n `20`; unknown avg `0.0903` n `755`
- 24h: commodity avg `-0.3773` n `12`; crypto_alt avg `3.1937` n `230`; crypto_major avg `2.6688` n `8`; equity avg `1.6972` n `98`; fx avg `-0.1002` n `6`; index avg `0.3544` n `25`; metal avg `0.6312` n `20`; unknown avg `0.1568` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0776`, n `666`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0771`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0767`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.069`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
