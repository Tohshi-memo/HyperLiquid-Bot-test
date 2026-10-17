# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T02:52:25.585505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `13`; crypto_alt avg `0.1369` n `236`; crypto_major avg `0.1773` n `8`; equity avg `0.0681` n `151`; fx avg `0.0007` n `6`; index avg `0.0137` n `26`; metal avg `-0.0017` n `20`; unknown avg `0.732` n `1193`
- 1h: commodity avg `0.0134` n `13`; crypto_alt avg `0.107` n `236`; crypto_major avg `0.04` n `8`; equity avg `0.0267` n `151`; fx avg `-0.0084` n `6`; index avg `0.0168` n `26`; metal avg `0.0083` n `20`; unknown avg `-0.2306` n `1191`
- 4h: commodity avg `0.1536` n `13`; crypto_alt avg `-0.2303` n `236`; crypto_major avg `-0.2754` n `8`; equity avg `0.2742` n `151`; fx avg `0.0124` n `6`; index avg `0.0114` n `26`; metal avg `-0.0096` n `20`; unknown avg `0.0914` n `1183`
- 24h: commodity avg `0.6701` n `13`; crypto_alt avg `-1.1667` n `236`; crypto_major avg `-1.0769` n `8`; equity avg `-3.8379` n `151`; fx avg `-0.0083` n `6`; index avg `-0.6183` n `26`; metal avg `-0.2037` n `20`; unknown avg `40.3031` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1703`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.117`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.077`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
