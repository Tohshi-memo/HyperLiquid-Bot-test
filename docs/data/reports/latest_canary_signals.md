# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T17:37:25.121031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0319` n `13`; crypto_alt avg `-0.0719` n `236`; crypto_major avg `0.0049` n `8`; equity avg `0.0161` n `151`; fx avg `-0.0017` n `6`; index avg `0.0032` n `26`; metal avg `0.0024` n `20`; unknown avg `1.1492` n `1193`
- 1h: commodity avg `0.0124` n `13`; crypto_alt avg `-0.1292` n `236`; crypto_major avg `0.0059` n `8`; equity avg `-0.0466` n `151`; fx avg `-0.0047` n `6`; index avg `-0.0209` n `26`; metal avg `-0.0048` n `20`; unknown avg `3.3125` n `1167`
- 4h: commodity avg `0.0911` n `13`; crypto_alt avg `-0.7086` n `236`; crypto_major avg `-0.3767` n `8`; equity avg `-0.2572` n `151`; fx avg `-0.0306` n `6`; index avg `-0.0673` n `26`; metal avg `-0.0474` n `20`; unknown avg `3.2815` n `1135`
- 24h: commodity avg `-0.0515` n `13`; crypto_alt avg `-1.9525` n `236`; crypto_major avg `-0.7198` n `8`; equity avg `-1.0391` n `151`; fx avg `-0.0172` n `6`; index avg `-0.1816` n `26`; metal avg `-0.0414` n `20`; unknown avg `3.4719` n `1027`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.171`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1476`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1132`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0716`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
