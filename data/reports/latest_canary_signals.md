# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T23:37:33.520039+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `0.5135` n `228`; crypto_major avg `0.5965` n `8`; equity avg `0.1507` n `88`; fx avg `-0.0097` n `6`; index avg `0.0031` n `23`; metal avg `0.015` n `20`; unknown avg `0.1958` n `764`
- 1h: commodity avg `-0.1065` n `12`; crypto_alt avg `0.5321` n `228`; crypto_major avg `0.8259` n `8`; equity avg `0.0696` n `88`; fx avg `-0.0036` n `6`; index avg `-0.0245` n `23`; metal avg `-0.0111` n `20`; unknown avg `0.5844` n `762`
- 4h: commodity avg `-0.452` n `12`; crypto_alt avg `-0.0764` n `228`; crypto_major avg `0.2601` n `8`; equity avg `0.3492` n `88`; fx avg `-0.0607` n `6`; index avg `0.116` n `23`; metal avg `-0.173` n `20`; unknown avg `0.8594` n `762`
- 24h: commodity avg `-0.2479` n `12`; crypto_alt avg `-0.1163` n `228`; crypto_major avg `-0.2402` n `8`; equity avg `0.4892` n `88`; fx avg `-0.1036` n `6`; index avg `0.1247` n `23`; metal avg `-0.1683` n `20`; unknown avg `15.3273` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
