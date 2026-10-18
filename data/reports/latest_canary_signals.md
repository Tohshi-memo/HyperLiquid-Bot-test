# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T14:22:28.586743+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `13`; crypto_alt avg `0.5149` n `237`; crypto_major avg `0.2953` n `8`; equity avg `0.0522` n `151`; fx avg `-0.0046` n `6`; index avg `-0.0034` n `26`; metal avg `-0.0059` n `20`; unknown avg `0.0967` n `1193`
- 1h: commodity avg `0.0282` n `13`; crypto_alt avg `-0.9309` n `237`; crypto_major avg `-0.7178` n `8`; equity avg `-0.2515` n `151`; fx avg `0.0003` n `6`; index avg `-0.0624` n `26`; metal avg `-0.0418` n `20`; unknown avg `0.0267` n `1189`
- 4h: commodity avg `-0.0319` n `13`; crypto_alt avg `-0.6867` n `237`; crypto_major avg `-1.0146` n `8`; equity avg `-0.3985` n `151`; fx avg `0.0044` n `6`; index avg `-0.0916` n `26`; metal avg `-0.0372` n `20`; unknown avg `-0.3104` n `1183`
- 24h: commodity avg `0.0422` n `13`; crypto_alt avg `-2.8743` n `236`; crypto_major avg `-0.9754` n `8`; equity avg `-0.9297` n `151`; fx avg `-0.0359` n `6`; index avg `-0.1303` n `26`; metal avg `-0.064` n `20`; unknown avg `0.5768` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2083`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1382`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1216`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.104`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0806`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
