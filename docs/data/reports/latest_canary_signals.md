# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T18:52:56.609433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.0451` n `228`; crypto_major avg `-0.1808` n `8`; equity avg `-0.1923` n `86`; fx avg `0.0044` n `6`; index avg `-0.0184` n `23`; metal avg `-0.0313` n `20`; unknown avg `0.2297` n `766`
- 1h: commodity avg `-0.0804` n `12`; crypto_alt avg `-0.439` n `228`; crypto_major avg `-0.4607` n `8`; equity avg `-0.6847` n `86`; fx avg `0.0061` n `6`; index avg `-0.1122` n `23`; metal avg `-0.1042` n `20`; unknown avg `-0.0561` n `765`
- 4h: commodity avg `-0.1041` n `12`; crypto_alt avg `1.1054` n `228`; crypto_major avg `0.6298` n `8`; equity avg `-0.1281` n `86`; fx avg `-0.0395` n `6`; index avg `-0.0288` n `23`; metal avg `-0.1636` n `20`; unknown avg `-0.1404` n `765`
- 24h: commodity avg `-0.5912` n `12`; crypto_alt avg `2.311` n `228`; crypto_major avg `1.8852` n `8`; equity avg `-0.9939` n `86`; fx avg `-0.0761` n `6`; index avg `-0.3209` n `23`; metal avg `0.4388` n `20`; unknown avg `0.2201` n `701`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2139`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
