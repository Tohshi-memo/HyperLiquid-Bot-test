# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T14:37:25.178181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0163` n `12`; crypto_alt avg `-0.147` n `228`; crypto_major avg `-0.0781` n `8`; equity avg `-0.0188` n `88`; fx avg `0.0006` n `6`; index avg `-0.0084` n `23`; metal avg `0.0041` n `20`; unknown avg `-0.0441` n `764`
- 1h: commodity avg `0.0123` n `12`; crypto_alt avg `0.2361` n `228`; crypto_major avg `0.2066` n `8`; equity avg `0.0638` n `88`; fx avg `-0.0015` n `6`; index avg `-0.0038` n `23`; metal avg `0.0133` n `20`; unknown avg `-0.0089` n `764`
- 4h: commodity avg `0.0887` n `12`; crypto_alt avg `0.4781` n `228`; crypto_major avg `0.516` n `8`; equity avg `0.1073` n `88`; fx avg `0.0094` n `6`; index avg `-0.0034` n `23`; metal avg `0.0179` n `20`; unknown avg `0.2681` n `764`
- 24h: commodity avg `0.2946` n `12`; crypto_alt avg `1.7655` n `228`; crypto_major avg `1.6132` n `8`; equity avg `1.0095` n `87`; fx avg `0.0303` n `6`; index avg `-0.0204` n `23`; metal avg `0.0804` n `20`; unknown avg `0.2313` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2056`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
