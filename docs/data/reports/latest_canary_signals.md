# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T17:07:27.527550+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `13`; crypto_alt avg `-0.3512` n `236`; crypto_major avg `-0.1916` n `8`; equity avg `-0.0489` n `151`; fx avg `0.0041` n `6`; index avg `-0.018` n `26`; metal avg `-0.0083` n `20`; unknown avg `2.7169` n `1167`
- 1h: commodity avg `-0.0284` n `13`; crypto_alt avg `-0.6113` n `236`; crypto_major avg `-0.3357` n `8`; equity avg `-0.0209` n `151`; fx avg `-0.0021` n `6`; index avg `-0.022` n `26`; metal avg `-0.0188` n `20`; unknown avg `3.1917` n `1159`
- 4h: commodity avg `0.0721` n `13`; crypto_alt avg `-1.1424` n `236`; crypto_major avg `-0.641` n `8`; equity avg `-0.282` n `151`; fx avg `-0.0258` n `6`; index avg `-0.0664` n `26`; metal avg `-0.0418` n `20`; unknown avg `2.5584` n `1135`
- 24h: commodity avg `0.1054` n `13`; crypto_alt avg `-2.1121` n `236`; crypto_major avg `-0.7141` n `8`; equity avg `-0.9719` n `151`; fx avg `-0.0028` n `6`; index avg `-0.187` n `26`; metal avg `-0.0197` n `20`; unknown avg `4.1383` n `1027`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1713`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1468`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1129`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0717`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
