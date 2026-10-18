# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T19:22:29.213749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0082` n `13`; crypto_alt avg `-0.3106` n `237`; crypto_major avg `-0.1902` n `8`; equity avg `-0.0351` n `151`; fx avg `-0.0059` n `6`; index avg `0.0019` n `26`; metal avg `-0.0025` n `20`; unknown avg `3.3946` n `1194`
- 1h: commodity avg `0.0166` n `13`; crypto_alt avg `-0.3432` n `237`; crypto_major avg `-0.0517` n `8`; equity avg `-0.0417` n `151`; fx avg `-0.0032` n `6`; index avg `0.0012` n `26`; metal avg `0.0081` n `20`; unknown avg `5.1145` n `1176`
- 4h: commodity avg `0.0195` n `13`; crypto_alt avg `-0.7856` n `237`; crypto_major avg `-0.3284` n `8`; equity avg `-0.1916` n `151`; fx avg `0.0072` n `6`; index avg `-0.0316` n `26`; metal avg `0.0092` n `20`; unknown avg `-0.3355` n `1144`
- 24h: commodity avg `-0.0148` n `13`; crypto_alt avg `-3.9609` n `236`; crypto_major avg `-1.5568` n `8`; equity avg `-1.121` n `151`; fx avg `0.0001` n `6`; index avg `-0.1496` n `26`; metal avg `-0.0401` n `20`; unknown avg `0.8105` n `1007`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2105`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1404`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1349`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1126`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0803`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
