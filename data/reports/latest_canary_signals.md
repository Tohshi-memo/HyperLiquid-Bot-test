# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T20:07:39.136911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0262` n `12`; crypto_alt avg `0.3037` n `228`; crypto_major avg `0.2474` n `8`; equity avg `0.0356` n `85`; fx avg `0.0016` n `6`; index avg `0.016` n `23`; metal avg `0.0499` n `20`; unknown avg `1.5971` n `717`
- 1h: commodity avg `0.0074` n `12`; crypto_alt avg `0.1716` n `228`; crypto_major avg `0.146` n `8`; equity avg `0.0368` n `85`; fx avg `0.0248` n `6`; index avg `0.0393` n `23`; metal avg `-0.0082` n `20`; unknown avg `0.1154` n `717`
- 4h: commodity avg `0.0091` n `12`; crypto_alt avg `-0.3722` n `228`; crypto_major avg `0.0956` n `8`; equity avg `-0.0661` n `85`; fx avg `-0.0066` n `6`; index avg `-0.0035` n `23`; metal avg `0.1323` n `20`; unknown avg `-0.5166` n `717`
- 24h: commodity avg `-0.959` n `12`; crypto_alt avg `-0.7965` n `228`; crypto_major avg `-0.4569` n `8`; equity avg `-0.649` n `85`; fx avg `0.1062` n `6`; index avg `0.0755` n `23`; metal avg `0.3235` n `18`; unknown avg `0.4627` n `639`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
