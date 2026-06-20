# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T17:37:29.670163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `-0.456` n `228`; crypto_major avg `-0.3326` n `8`; equity avg `-0.0744` n `78`; fx avg `-0.1393` n `6`; index avg `-0.0125` n `23`; metal avg `-0.011` n `18`; unknown avg `-0.1101` n `701`
- 1h: commodity avg `-0.0208` n `12`; crypto_alt avg `-0.3061` n `228`; crypto_major avg `-0.4255` n `8`; equity avg `-0.0909` n `78`; fx avg `-0.1201` n `6`; index avg `-0.0113` n `23`; metal avg `-0.0391` n `18`; unknown avg `-0.2182` n `701`
- 4h: commodity avg `-0.0338` n `12`; crypto_alt avg `0.341` n `228`; crypto_major avg `-0.0026` n `8`; equity avg `0.1264` n `78`; fx avg `-0.0887` n `6`; index avg `-0.017` n `23`; metal avg `-0.0225` n `18`; unknown avg `0.2244` n `701`
- 24h: commodity avg `0.3739` n `12`; crypto_alt avg `-0.0234` n `228`; crypto_major avg `0.641` n `8`; equity avg `0.3075` n `78`; fx avg `-0.078` n `6`; index avg `0.0117` n `23`; metal avg `0.113` n `18`; unknown avg `-0.2189` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
