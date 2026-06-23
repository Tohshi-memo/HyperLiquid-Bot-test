# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T22:07:31.351629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0074` n `12`; crypto_alt avg `0.2203` n `228`; crypto_major avg `0.2358` n `8`; equity avg `0.0051` n `86`; fx avg `-0.0171` n `6`; index avg `0.0219` n `23`; metal avg `-0.0372` n `20`; unknown avg `-0.2529` n `764`
- 1h: commodity avg `-0.017` n `12`; crypto_alt avg `0.2302` n `228`; crypto_major avg `0.3625` n `8`; equity avg `0.0779` n `86`; fx avg `-0.0137` n `6`; index avg `0.075` n `23`; metal avg `-0.0027` n `20`; unknown avg `0.2661` n `764`
- 4h: commodity avg `-0.0416` n `12`; crypto_alt avg `1.1224` n `228`; crypto_major avg `0.7804` n `8`; equity avg `-0.0037` n `86`; fx avg `-0.0091` n `6`; index avg `0.084` n `23`; metal avg `-0.0602` n `20`; unknown avg `1.4679` n `756`
- 24h: commodity avg `-0.4293` n `12`; crypto_alt avg `-2.2302` n `228`; crypto_major avg `-3.183` n `8`; equity avg `-3.2391` n `86`; fx avg `-0.1664` n `6`; index avg `-0.8539` n `23`; metal avg `-1.1971` n `20`; unknown avg `1.812` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
