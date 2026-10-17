# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T19:37:27.542147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `13`; crypto_alt avg `0.07` n `236`; crypto_major avg `0.0389` n `8`; equity avg `0.0056` n `151`; fx avg `0.0003` n `6`; index avg `-0.0066` n `26`; metal avg `0.0048` n `20`; unknown avg `-0.0446` n `1169`
- 1h: commodity avg `-0.0049` n `13`; crypto_alt avg `0.2601` n `236`; crypto_major avg `0.0745` n `8`; equity avg `0.0416` n `151`; fx avg `0.0026` n `6`; index avg `0.0011` n `26`; metal avg `0.0069` n `20`; unknown avg `2.3613` n `1159`
- 4h: commodity avg `-0.0291` n `13`; crypto_alt avg `0.4831` n `236`; crypto_major avg `0.2112` n `8`; equity avg `0.116` n `151`; fx avg `-0.0104` n `6`; index avg `-0.0126` n `26`; metal avg `-0.0093` n `20`; unknown avg `0.9789` n `1113`
- 24h: commodity avg `0.0546` n `13`; crypto_alt avg `-0.5647` n `236`; crypto_major avg `0.1858` n `8`; equity avg `0.0379` n `151`; fx avg `-0.016` n `6`; index avg `-0.0095` n `26`; metal avg `-0.0395` n `20`; unknown avg `4.9166` n `987`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1721`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.148`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1128`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0724`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
