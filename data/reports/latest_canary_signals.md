# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T18:37:25.599610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `0.0606` n `228`; crypto_major avg `0.0914` n `8`; equity avg `0.0216` n `88`; fx avg `0.0006` n `6`; index avg `-0.0228` n `23`; metal avg `-0.0078` n `20`; unknown avg `-0.0871` n `764`
- 1h: commodity avg `-0.0518` n `12`; crypto_alt avg `-0.1881` n `228`; crypto_major avg `-0.2624` n `8`; equity avg `0.0212` n `88`; fx avg `0.003` n `6`; index avg `-0.0144` n `23`; metal avg `0.001` n `20`; unknown avg `-0.1402` n `764`
- 4h: commodity avg `-0.1696` n `12`; crypto_alt avg `-0.2654` n `228`; crypto_major avg `-0.4403` n `8`; equity avg `-0.1264` n `88`; fx avg `0.005` n `6`; index avg `-0.0436` n `23`; metal avg `-0.0457` n `20`; unknown avg `0.0448` n `764`
- 24h: commodity avg `0.2672` n `12`; crypto_alt avg `0.0823` n `228`; crypto_major avg `0.071` n `8`; equity avg `0.7631` n `88`; fx avg `0.0821` n `6`; index avg `-0.0702` n `23`; metal avg `0.0626` n `20`; unknown avg `-0.007` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.209`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
