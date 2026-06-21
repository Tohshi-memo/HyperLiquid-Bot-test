# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T02:52:26.492913+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `0.0557` n `228`; crypto_major avg `-0.0523` n `8`; equity avg `-0.0266` n `78`; fx avg `0.0006` n `6`; index avg `0.0006` n `23`; metal avg `0.001` n `18`; unknown avg `-0.1379` n `702`
- 1h: commodity avg `0.005` n `12`; crypto_alt avg `-0.1463` n `228`; crypto_major avg `-0.1741` n `8`; equity avg `-0.0097` n `78`; fx avg `-0.0134` n `6`; index avg `0.0074` n `23`; metal avg `0.0074` n `18`; unknown avg `-0.4661` n `702`
- 4h: commodity avg `0.0193` n `12`; crypto_alt avg `0.1505` n `228`; crypto_major avg `-0.3204` n `8`; equity avg `0.0171` n `78`; fx avg `-0.01` n `6`; index avg `-0.0245` n `23`; metal avg `-0.0147` n `18`; unknown avg `1.3017` n `701`
- 24h: commodity avg `0.1962` n `12`; crypto_alt avg `1.8091` n `228`; crypto_major avg `1.6507` n `8`; equity avg `0.4009` n `78`; fx avg `0.0404` n `6`; index avg `-0.0122` n `23`; metal avg `-0.0255` n `18`; unknown avg `1.7582` n `557`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
