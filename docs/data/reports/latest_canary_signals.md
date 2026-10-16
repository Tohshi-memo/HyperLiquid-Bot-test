# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T05:37:31.852354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0594` n `13`; crypto_alt avg `-0.1152` n `236`; crypto_major avg `-0.1286` n `8`; equity avg `-0.2477` n `151`; fx avg `-0.02` n `6`; index avg `-0.0301` n `26`; metal avg `-0.0209` n `20`; unknown avg `3.8694` n `1136`
- 1h: commodity avg `-0.0643` n `13`; crypto_alt avg `0.184` n `236`; crypto_major avg `0.1916` n `8`; equity avg `-0.1465` n `151`; fx avg `-0.0667` n `6`; index avg `-0.0129` n `26`; metal avg `-0.0478` n `20`; unknown avg `3.7363` n `1134`
- 4h: commodity avg `-0.0939` n `13`; crypto_alt avg `0.3889` n `236`; crypto_major avg `0.2358` n `8`; equity avg `0.4345` n `151`; fx avg `-0.0595` n `6`; index avg `0.0817` n `26`; metal avg `0.2402` n `20`; unknown avg `0.4029` n `1124`
- 24h: commodity avg `-0.0878` n `13`; crypto_alt avg `4.0548` n `236`; crypto_major avg `2.09` n `8`; equity avg `2.5074` n `151`; fx avg `-0.0365` n `6`; index avg `0.4289` n `26`; metal avg `0.5218` n `20`; unknown avg `25.8876` n `906`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1038`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0959`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0927`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0789`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0715`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0651`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
