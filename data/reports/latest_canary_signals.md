# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T00:52:38.444520+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.028` n `13`; crypto_alt avg `-0.1302` n `235`; crypto_major avg `0.1097` n `8`; equity avg `-0.0348` n `144`; fx avg `0.0242` n `6`; index avg `-0.0149` n `26`; metal avg `0.068` n `20`; unknown avg `-0.0023` n `1079`
- 1h: commodity avg `0.0296` n `13`; crypto_alt avg `-0.3488` n `235`; crypto_major avg `0.153` n `8`; equity avg `0.0003` n `144`; fx avg `-0.0089` n `6`; index avg `-0.0102` n `26`; metal avg `0.1042` n `20`; unknown avg `0.0329` n `1071`
- 4h: commodity avg `0.0033` n `13`; crypto_alt avg `-0.1429` n `235`; crypto_major avg `0.1891` n `8`; equity avg `0.1091` n `144`; fx avg `0.0174` n `6`; index avg `-0.0054` n `26`; metal avg `0.0719` n `20`; unknown avg `-0.1597` n `1019`
- 24h: commodity avg `-0.1684` n `13`; crypto_alt avg `-0.271` n `235`; crypto_major avg `0.0093` n `8`; equity avg `0.0744` n `144`; fx avg `-0.0767` n `6`; index avg `0.0826` n `26`; metal avg `0.0482` n `20`; unknown avg `625.5036` n `800`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1933`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
