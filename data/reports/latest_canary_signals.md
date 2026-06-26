# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T18:07:29.078379+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0451` n `12`; crypto_alt avg `-0.0184` n `228`; crypto_major avg `0.1437` n `8`; equity avg `-0.1353` n `86`; fx avg `0.0068` n `6`; index avg `-0.0193` n `23`; metal avg `-0.0351` n `20`; unknown avg `0.1143` n `765`
- 1h: commodity avg `0.011` n `12`; crypto_alt avg `-0.0993` n `228`; crypto_major avg `-0.1087` n `8`; equity avg `-0.2806` n `86`; fx avg `-0.0006` n `6`; index avg `-0.0481` n `23`; metal avg `-0.0853` n `20`; unknown avg `0.0401` n `765`
- 4h: commodity avg `0.0113` n `12`; crypto_alt avg `1.6383` n `228`; crypto_major avg `1.3494` n `8`; equity avg `0.3547` n `86`; fx avg `-0.0534` n `6`; index avg `0.0506` n `23`; metal avg `-0.0041` n `20`; unknown avg `0.1369` n `765`
- 24h: commodity avg `-0.5429` n `12`; crypto_alt avg `2.2264` n `228`; crypto_major avg `2.1556` n `8`; equity avg `-0.4353` n `86`; fx avg `-0.0749` n `6`; index avg `-0.2226` n `23`; metal avg `0.5783` n `20`; unknown avg `0.3232` n `701`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2122`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2111`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
