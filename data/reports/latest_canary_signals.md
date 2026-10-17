# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T22:52:27.650815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `13`; crypto_alt avg `0.2742` n `236`; crypto_major avg `0.1656` n `8`; equity avg `-0.0861` n `151`; fx avg `0.0084` n `6`; index avg `0.0137` n `26`; metal avg `0.0027` n `20`; unknown avg `0.0019` n `1193`
- 1h: commodity avg `-0.0371` n `13`; crypto_alt avg `0.6963` n `236`; crypto_major avg `0.493` n `8`; equity avg `0.084` n `151`; fx avg `0.005` n `6`; index avg `0.0254` n `26`; metal avg `0.035` n `20`; unknown avg `0.3607` n `1191`
- 4h: commodity avg `-0.0491` n `13`; crypto_alt avg `-0.7476` n `236`; crypto_major avg `-0.4922` n `8`; equity avg `-1.0285` n `151`; fx avg `0.0004` n `6`; index avg `-0.1311` n `26`; metal avg `-0.055` n `20`; unknown avg `0.3415` n `1139`
- 24h: commodity avg `0.0309` n `13`; crypto_alt avg `-2.2727` n `236`; crypto_major avg `-1.1708` n `8`; equity avg `-0.8518` n `151`; fx avg `-0.0205` n `6`; index avg `-0.1304` n `26`; metal avg `-0.0969` n `20`; unknown avg `4.0945` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1653`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1396`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1076`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0725`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
