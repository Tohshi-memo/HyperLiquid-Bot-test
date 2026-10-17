# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T22:37:30.290928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.009` n `13`; crypto_alt avg `0.04` n `236`; crypto_major avg `0.0171` n `8`; equity avg `0.0883` n `151`; fx avg `-0.0015` n `6`; index avg `-0.0078` n `26`; metal avg `0.0152` n `20`; unknown avg `0.8224` n `1193`
- 1h: commodity avg `-0.0338` n `13`; crypto_alt avg `0.8187` n `236`; crypto_major avg `0.6167` n `8`; equity avg `0.7747` n `151`; fx avg `-0.0051` n `6`; index avg `0.0435` n `26`; metal avg `0.0572` n `20`; unknown avg `3.5879` n `1191`
- 4h: commodity avg `-0.0393` n `13`; crypto_alt avg `-0.8958` n `236`; crypto_major avg `-0.6302` n `8`; equity avg `-0.9072` n `151`; fx avg `-0.0049` n `6`; index avg `-0.1368` n `26`; metal avg `-0.0578` n `20`; unknown avg `0.8863` n `1139`
- 24h: commodity avg `0.028` n `13`; crypto_alt avg `-2.4342` n `236`; crypto_major avg `-1.3081` n `8`; equity avg `-0.7857` n `151`; fx avg `-0.0274` n `6`; index avg `-0.1293` n `26`; metal avg `-0.0985` n `20`; unknown avg `5.7113` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1659`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1399`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1081`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0721`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
