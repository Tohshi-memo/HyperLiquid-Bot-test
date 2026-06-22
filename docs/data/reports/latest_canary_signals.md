# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T22:07:27.307286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `12`; crypto_alt avg `0.1274` n `228`; crypto_major avg `0.1275` n `8`; equity avg `0.0287` n `86`; fx avg `0.0057` n `6`; index avg `-0.0118` n `23`; metal avg `0.0027` n `20`; unknown avg `0.1979` n `716`
- 1h: commodity avg `0.0074` n `12`; crypto_alt avg `-0.2093` n `228`; crypto_major avg `-0.1755` n `8`; equity avg `0.01` n `86`; fx avg `-0.0355` n `6`; index avg `0.0061` n `23`; metal avg `0.0088` n `20`; unknown avg `-0.2286` n `716`
- 4h: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.8393` n `228`; crypto_major avg `-0.7499` n `8`; equity avg `-0.2993` n `86`; fx avg `-0.021` n `6`; index avg `-0.0544` n `23`; metal avg `0.0852` n `20`; unknown avg `-0.1426` n `708`
- 24h: commodity avg `-0.9307` n `12`; crypto_alt avg `0.0823` n `228`; crypto_major avg `0.3445` n `8`; equity avg `-0.4264` n `85`; fx avg `0.0698` n `6`; index avg `0.1661` n `23`; metal avg `0.4114` n `18`; unknown avg `0.473` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
