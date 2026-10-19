# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T03:07:26.621648+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0117` n `13`; crypto_alt avg `-0.1395` n `237`; crypto_major avg `-0.1118` n `8`; equity avg `0.012` n `151`; fx avg `0.0169` n `6`; index avg `0.0129` n `26`; metal avg `0.035` n `20`; unknown avg `0.5154` n `1192`
- 1h: commodity avg `0.0159` n `13`; crypto_alt avg `-0.1732` n `237`; crypto_major avg `0.0701` n `8`; equity avg `0.3441` n `151`; fx avg `-0.0111` n `6`; index avg `0.0409` n `26`; metal avg `0.0059` n `20`; unknown avg `-0.3118` n `1192`
- 4h: commodity avg `-0.1056` n `13`; crypto_alt avg `1.2031` n `237`; crypto_major avg `1.0487` n `8`; equity avg `1.8267` n `151`; fx avg `-0.0066` n `6`; index avg `0.3155` n `26`; metal avg `0.1117` n `20`; unknown avg `2.3431` n `1128`
- 24h: commodity avg `-0.4113` n `13`; crypto_alt avg `-0.2571` n `237`; crypto_major avg `0.6214` n `8`; equity avg `2.6695` n `151`; fx avg `-0.0184` n `6`; index avg `0.4937` n `26`; metal avg `0.2993` n `20`; unknown avg `3.2112` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2032`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1493`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1064`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0984`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0633`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0606`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
