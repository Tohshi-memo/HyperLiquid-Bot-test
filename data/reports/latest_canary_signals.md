# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T23:37:30.389065+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `13`; crypto_alt avg `-0.0413` n `236`; crypto_major avg `-0.0066` n `8`; equity avg `-0.0047` n `151`; fx avg `-0.0005` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0112` n `20`; unknown avg `0.3007` n `1193`
- 1h: commodity avg `-0.0217` n `13`; crypto_alt avg `0.1269` n `236`; crypto_major avg `0.0355` n `8`; equity avg `0.0919` n `151`; fx avg `0.0088` n `6`; index avg `0.0336` n `26`; metal avg `0.0023` n `20`; unknown avg `-0.1305` n `1191`
- 4h: commodity avg `-0.0562` n `13`; crypto_alt avg `-1.0262` n `236`; crypto_major avg `-0.6688` n `8`; equity avg `-0.8576` n `151`; fx avg `0.0012` n `6`; index avg `-0.1045` n `26`; metal avg `-0.0624` n `20`; unknown avg `0.6053` n `1171`
- 24h: commodity avg `-0.0395` n `13`; crypto_alt avg `-2.4345` n `236`; crypto_major avg `-1.2741` n `8`; equity avg `-0.6104` n `151`; fx avg `-0.0284` n `6`; index avg `-0.0824` n `26`; metal avg `-0.0846` n `20`; unknown avg `1.8171` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1638`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1362`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1049`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1049`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0732`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
