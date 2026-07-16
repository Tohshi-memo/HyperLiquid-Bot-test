# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T02:37:24.320163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0171` n `12`; crypto_alt avg `0.0727` n `230`; crypto_major avg `0.0854` n `8`; equity avg `0.0645` n `94`; fx avg `0.0041` n `6`; index avg `0.06` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.048` n `768`
- 1h: commodity avg `-0.0121` n `12`; crypto_alt avg `0.2692` n `230`; crypto_major avg `0.1128` n `8`; equity avg `0.2699` n `94`; fx avg `-0.0207` n `6`; index avg `0.0662` n `25`; metal avg `-0.0281` n `20`; unknown avg `-0.2273` n `768`
- 4h: commodity avg `-0.1086` n `12`; crypto_alt avg `-0.0659` n `230`; crypto_major avg `-0.3359` n `8`; equity avg `-0.2148` n `94`; fx avg `-0.0245` n `6`; index avg `-0.0965` n `25`; metal avg `-0.2209` n `20`; unknown avg `-0.2623` n `766`
- 24h: commodity avg `-0.0921` n `12`; crypto_alt avg `0.5137` n `230`; crypto_major avg `0.7508` n `8`; equity avg `-1.9834` n `93`; fx avg `0.1496` n `6`; index avg `-0.4269` n `25`; metal avg `-0.0723` n `20`; unknown avg `0.0611` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
