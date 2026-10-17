# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T19:52:35.549670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0473` n `13`; crypto_alt avg `0.1697` n `236`; crypto_major avg `0.1108` n `8`; equity avg `0.0014` n `151`; fx avg `-0.0006` n `6`; index avg `-0.0027` n `26`; metal avg `0.0025` n `20`; unknown avg `0.1667` n `1193`
- 1h: commodity avg `-0.0493` n `13`; crypto_alt avg `0.3066` n `236`; crypto_major avg `0.1587` n `8`; equity avg `0.0047` n `151`; fx avg `-0.0011` n `6`; index avg `-0.0096` n `26`; metal avg `0.0096` n `20`; unknown avg `3.704` n `1159`
- 4h: commodity avg `-0.0263` n `13`; crypto_alt avg `1.0092` n `236`; crypto_major avg `0.5782` n `8`; equity avg `0.1634` n `151`; fx avg `-0.0153` n `6`; index avg `0.0061` n `26`; metal avg `-0.0001` n `20`; unknown avg `1.1803` n `1113`
- 24h: commodity avg `0.0339` n `13`; crypto_alt avg `-0.6289` n `236`; crypto_major avg `0.0639` n `8`; equity avg `-0.0072` n `151`; fx avg `-0.0227` n `6`; index avg `-0.0271` n `26`; metal avg `-0.0253` n `20`; unknown avg `4.7688` n `987`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1717`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1484`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1131`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0725`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
