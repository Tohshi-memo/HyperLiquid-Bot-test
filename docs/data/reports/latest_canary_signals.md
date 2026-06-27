# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T23:47:44.161251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `0.0365` n `228`; crypto_major avg `0.0042` n `8`; equity avg `0.0065` n `88`; fx avg `-0.0063` n `6`; index avg `-0.0074` n `23`; metal avg `0.0004` n `20`; unknown avg `58.6122` n `764`
- 1h: commodity avg `0.0741` n `12`; crypto_alt avg `-0.1839` n `228`; crypto_major avg `-0.4178` n `8`; equity avg `-0.0721` n `88`; fx avg `-0.0096` n `6`; index avg `-0.0195` n `23`; metal avg `-0.0092` n `20`; unknown avg `-0.0947` n `764`
- 4h: commodity avg `0.1531` n `12`; crypto_alt avg `-0.1755` n `228`; crypto_major avg `-0.4655` n `8`; equity avg `0.0217` n `88`; fx avg `0.0002` n `6`; index avg `-0.0472` n `23`; metal avg `0.008` n `20`; unknown avg `-0.5064` n `764`
- 24h: commodity avg `0.1469` n `12`; crypto_alt avg `-0.8294` n `228`; crypto_major avg `-1.2261` n `8`; equity avg `0.2274` n `88`; fx avg `0.0372` n `6`; index avg `-0.0753` n `23`; metal avg `-0.0782` n `20`; unknown avg `-0.9437` n `716`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2096`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
