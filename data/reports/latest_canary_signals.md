# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T08:22:31.157883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0118` n `13`; crypto_alt avg `-0.0378` n `236`; crypto_major avg `-0.0621` n `8`; equity avg `0.0015` n `151`; fx avg `-0.0008` n `6`; index avg `0.004` n `26`; metal avg `0.0172` n `20`; unknown avg `-0.0412` n `1114`
- 1h: commodity avg `-0.0252` n `13`; crypto_alt avg `-0.523` n `236`; crypto_major avg `-0.1746` n `8`; equity avg `-0.1691` n `151`; fx avg `0.002` n `6`; index avg `-0.0184` n `26`; metal avg `-0.0425` n `20`; unknown avg `-0.1492` n `1068`
- 4h: commodity avg `0.0372` n `13`; crypto_alt avg `0.2277` n `236`; crypto_major avg `0.2819` n `8`; equity avg `-0.406` n `151`; fx avg `-0.1082` n `6`; index avg `-0.0732` n `26`; metal avg `-0.0508` n `20`; unknown avg `-0.1876` n `1048`
- 24h: commodity avg `0.0978` n `13`; crypto_alt avg `4.0249` n `236`; crypto_major avg `1.8673` n `8`; equity avg `2.8352` n `151`; fx avg `-0.0163` n `6`; index avg `0.3617` n `26`; metal avg `0.3365` n `20`; unknown avg `28.1998` n `864`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.0975`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0928`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0914`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0906`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
