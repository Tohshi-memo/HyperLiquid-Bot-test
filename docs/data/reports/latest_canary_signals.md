# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T14:07:33.788449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `0.0288` n `228`; crypto_major avg `-0.0347` n `8`; equity avg `-0.0448` n `88`; fx avg `-0.0061` n `6`; index avg `-0.0147` n `23`; metal avg `0.0069` n `20`; unknown avg `0.069` n `764`
- 1h: commodity avg `0.0431` n `12`; crypto_alt avg `0.1217` n `228`; crypto_major avg `0.1809` n `8`; equity avg `0.0458` n `88`; fx avg `-0.0084` n `6`; index avg `-0.0049` n `23`; metal avg `0.0012` n `20`; unknown avg `0.0537` n `764`
- 4h: commodity avg `0.1033` n `12`; crypto_alt avg `0.07` n `228`; crypto_major avg `0.0899` n `8`; equity avg `0.0535` n `88`; fx avg `-0.0092` n `6`; index avg `0.0051` n `23`; metal avg `-0.0091` n `20`; unknown avg `-0.6087` n `764`
- 24h: commodity avg `0.1258` n `12`; crypto_alt avg `-0.5448` n `228`; crypto_major avg `-1.2082` n `8`; equity avg `-0.0153` n `88`; fx avg `-0.0105` n `6`; index avg `-0.0665` n `23`; metal avg `-0.0362` n `20`; unknown avg `15.4367` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2001`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1854`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
