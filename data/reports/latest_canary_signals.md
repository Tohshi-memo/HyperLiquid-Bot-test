# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T00:52:29.003903+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `12`; crypto_alt avg `0.1048` n `228`; crypto_major avg `0.0845` n `8`; equity avg `0.0564` n `86`; fx avg `-0.0007` n `6`; index avg `-0.0477` n `23`; metal avg `0.0208` n `20`; unknown avg `-0.161` n `764`
- 1h: commodity avg `0.0123` n `12`; crypto_alt avg `0.4733` n `228`; crypto_major avg `0.3752` n `8`; equity avg `0.7032` n `86`; fx avg `0.021` n `6`; index avg `0.1007` n `23`; metal avg `0.0228` n `20`; unknown avg `0.0534` n `764`
- 4h: commodity avg `-0.0754` n `12`; crypto_alt avg `0.541` n `228`; crypto_major avg `0.8429` n `8`; equity avg `0.7545` n `86`; fx avg `0.0239` n `6`; index avg `0.1836` n `23`; metal avg `-0.0551` n `20`; unknown avg `0.1745` n `756`
- 24h: commodity avg `-0.4625` n `12`; crypto_alt avg `-1.7276` n `228`; crypto_major avg `-2.5558` n `8`; equity avg `-2.0591` n `86`; fx avg `-0.1748` n `6`; index avg `-0.6139` n `23`; metal avg `-1.2517` n `20`; unknown avg `0.5431` n `588`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
