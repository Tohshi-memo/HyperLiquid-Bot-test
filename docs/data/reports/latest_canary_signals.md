# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T18:07:25.965480+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `12`; crypto_alt avg `-0.2202` n `228`; crypto_major avg `-0.2737` n `8`; equity avg `-0.0101` n `88`; fx avg `-0.0005` n `6`; index avg `0.004` n `23`; metal avg `0.0073` n `20`; unknown avg `0.0225` n `764`
- 1h: commodity avg `-0.011` n `12`; crypto_alt avg `-0.3412` n `228`; crypto_major avg `-0.331` n `8`; equity avg `-0.0042` n `88`; fx avg `0.0017` n `6`; index avg `0.0041` n `23`; metal avg `-0.025` n `20`; unknown avg `-0.0855` n `764`
- 4h: commodity avg `-0.1817` n `12`; crypto_alt avg `-0.2598` n `228`; crypto_major avg `-0.4182` n `8`; equity avg `-0.1547` n `88`; fx avg `0.003` n `6`; index avg `-0.027` n `23`; metal avg `-0.0337` n `20`; unknown avg `0.0397` n `764`
- 24h: commodity avg `0.1596` n `12`; crypto_alt avg `-0.3524` n `228`; crypto_major avg `-0.3909` n `8`; equity avg `0.3768` n `88`; fx avg `0.0764` n `6`; index avg `-0.1253` n `23`; metal avg `0.0307` n `20`; unknown avg `0.0449` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2083`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
