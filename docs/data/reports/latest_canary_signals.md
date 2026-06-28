# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T04:37:28.241778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `-0.029` n `228`; crypto_major avg `-0.1808` n `8`; equity avg `-0.0524` n `88`; fx avg `0.0` n `6`; index avg `0.0057` n `23`; metal avg `-0.0049` n `20`; unknown avg `0.884` n `756`
- 1h: commodity avg `-0.0621` n `12`; crypto_alt avg `0.1356` n `228`; crypto_major avg `-0.1714` n `8`; equity avg `-0.0371` n `88`; fx avg `0.0052` n `6`; index avg `0.0097` n `23`; metal avg `-0.0043` n `20`; unknown avg `0.2453` n `756`
- 4h: commodity avg `-0.0391` n `12`; crypto_alt avg `0.2818` n `228`; crypto_major avg `-0.132` n `8`; equity avg `-0.1034` n `88`; fx avg `-0.009` n `6`; index avg `-0.0249` n `23`; metal avg `0.0254` n `20`; unknown avg `15.3839` n `714`
- 24h: commodity avg `0.2033` n `12`; crypto_alt avg `-0.6058` n `228`; crypto_major avg `-1.4728` n `8`; equity avg `0.0025` n `88`; fx avg `-0.0079` n `6`; index avg `-0.1108` n `23`; metal avg `-0.0315` n `20`; unknown avg `9.3372` n `666`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2216`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1864`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
