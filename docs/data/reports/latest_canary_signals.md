# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T10:22:19.065381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0092` n `12`; crypto_alt avg `-0.2162` n `228`; crypto_major avg `-0.1128` n `8`; equity avg `0.1021` n `67`; fx avg `0.0005` n `6`; index avg `-0.002` n `23`; metal avg `-0.0108` n `18`; unknown avg `0.0794` n `396`
- 1h: commodity avg `0.091` n `12`; crypto_alt avg `-0.3172` n `228`; crypto_major avg `-0.0967` n `8`; equity avg `0.0908` n `67`; fx avg `-0.0061` n `6`; index avg `-0.0033` n `23`; metal avg `0.0482` n `18`; unknown avg `-0.65` n `396`
- 4h: commodity avg `0.3842` n `12`; crypto_alt avg `0.0757` n `228`; crypto_major avg `0.762` n `8`; equity avg `0.3213` n `67`; fx avg `-0.0073` n `6`; index avg `0.0744` n `23`; metal avg `0.0646` n `18`; unknown avg `-0.6695` n `396`
- 24h: commodity avg `-2.5636` n `12`; crypto_alt avg `3.5676` n `228`; crypto_major avg `4.5456` n `8`; equity avg `2.6986` n `67`; fx avg `0.06` n `6`; index avg `1.5337` n `23`; metal avg `1.3845` n `18`; unknown avg `1.5084` n `386`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
