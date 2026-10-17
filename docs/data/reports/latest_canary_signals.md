# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T03:07:28.871384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `13`; crypto_alt avg `-0.052` n `236`; crypto_major avg `-0.0498` n `8`; equity avg `0.024` n `151`; fx avg `-0.0016` n `6`; index avg `0.0012` n `26`; metal avg `0.0065` n `20`; unknown avg `0.0695` n `1191`
- 1h: commodity avg `0.0058` n `13`; crypto_alt avg `-0.2056` n `236`; crypto_major avg `-0.114` n `8`; equity avg `-0.0202` n `151`; fx avg `0.0135` n `6`; index avg `0.0148` n `26`; metal avg `0.025` n `20`; unknown avg `-0.0466` n `1191`
- 4h: commodity avg `0.12` n `13`; crypto_alt avg `-0.2853` n `236`; crypto_major avg `-0.3376` n `8`; equity avg `0.4192` n `151`; fx avg `0.0033` n `6`; index avg `0.0231` n `26`; metal avg `0.0073` n `20`; unknown avg `0.2511` n `1183`
- 24h: commodity avg `0.6581` n `13`; crypto_alt avg `-1.2474` n `236`; crypto_major avg `-1.2324` n `8`; equity avg `-3.8836` n `151`; fx avg `-0.0246` n `6`; index avg `-0.6289` n `26`; metal avg `-0.2481` n `20`; unknown avg `40.3911` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1707`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1172`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0935`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0766`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0714`, n `666`, weak_sample_signal
