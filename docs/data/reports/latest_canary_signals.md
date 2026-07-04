# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T02:52:25.332457+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `0.0959` n `229`; crypto_major avg `0.3009` n `8`; equity avg `0.0636` n `88`; fx avg `-0.0382` n `6`; index avg `0.0144` n `25`; metal avg `0.0047` n `20`; unknown avg `-0.09` n `765`
- 1h: commodity avg `-0.003` n `12`; crypto_alt avg `0.2909` n `229`; crypto_major avg `0.3284` n `8`; equity avg `0.1197` n `88`; fx avg `-0.0231` n `6`; index avg `0.0139` n `25`; metal avg `0.0107` n `20`; unknown avg `-0.3753` n `763`
- 4h: commodity avg `-0.0089` n `12`; crypto_alt avg `-0.3593` n `229`; crypto_major avg `-0.0231` n `8`; equity avg `0.1477` n `88`; fx avg `-0.0177` n `6`; index avg `-0.0327` n `25`; metal avg `-0.0193` n `20`; unknown avg `0.0426` n `763`
- 24h: commodity avg `0.0069` n `12`; crypto_alt avg `2.1822` n `229`; crypto_major avg `2.8809` n `8`; equity avg `0.8784` n `88`; fx avg `-0.1594` n `6`; index avg `0.1795` n `25`; metal avg `-0.1836` n `20`; unknown avg `4.2872` n `737`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
