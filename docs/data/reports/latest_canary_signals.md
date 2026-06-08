# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T12:37:30.759038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.065` n `12`; crypto_alt avg `0.4664` n `228`; crypto_major avg `0.6244` n `8`; equity avg `0.2562` n `74`; fx avg `-0.0092` n `6`; index avg `0.0871` n `23`; metal avg `0.1086` n `18`; unknown avg `0.1709` n `517`
- 1h: commodity avg `-0.0039` n `12`; crypto_alt avg `-0.2196` n `228`; crypto_major avg `-0.3159` n `8`; equity avg `0.1595` n `74`; fx avg `-0.034` n `6`; index avg `0.1275` n `23`; metal avg `0.2148` n `18`; unknown avg `-2.5036` n `517`
- 4h: commodity avg `-0.8212` n `12`; crypto_alt avg `1.3653` n `228`; crypto_major avg `1.0052` n `8`; equity avg `1.1703` n `74`; fx avg `0.0139` n `6`; index avg `0.6771` n `23`; metal avg `1.1468` n `18`; unknown avg `-2.2067` n `517`
- 24h: commodity avg `-0.2794` n `12`; crypto_alt avg `2.9074` n `228`; crypto_major avg `3.5339` n `8`; equity avg `2.4374` n `74`; fx avg `-0.2945` n `6`; index avg `1.1322` n `23`; metal avg `0.4913` n `18`; unknown avg `-3.3365` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
