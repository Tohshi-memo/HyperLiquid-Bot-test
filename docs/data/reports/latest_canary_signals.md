# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T05:07:34.479519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0122` n `13`; crypto_alt avg `-0.2368` n `237`; crypto_major avg `-0.2793` n `8`; equity avg `-0.0374` n `151`; fx avg `-0.008` n `6`; index avg `0.0116` n `26`; metal avg `-0.0228` n `20`; unknown avg `-0.0421` n `1192`
- 1h: commodity avg `0.0046` n `13`; crypto_alt avg `-0.0468` n `237`; crypto_major avg `0.095` n `8`; equity avg `-0.0318` n `151`; fx avg `-0.0085` n `6`; index avg `0.0025` n `26`; metal avg `-0.0115` n `20`; unknown avg `6.7562` n `1190`
- 4h: commodity avg `-0.0868` n `13`; crypto_alt avg `-0.012` n `237`; crypto_major avg `0.317` n `8`; equity avg `0.778` n `151`; fx avg `-0.0398` n `6`; index avg `0.1746` n `26`; metal avg `0.1289` n `20`; unknown avg `5.9222` n `1184`
- 24h: commodity avg `-0.406` n `13`; crypto_alt avg `-0.1266` n `237`; crypto_major avg `0.8133` n `8`; equity avg `2.617` n `151`; fx avg `-0.0172` n `6`; index avg `0.5031` n `26`; metal avg `0.3137` n `20`; unknown avg `3.1179` n `901`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1986`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1441`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1172`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0975`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0729`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0728`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0681`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
