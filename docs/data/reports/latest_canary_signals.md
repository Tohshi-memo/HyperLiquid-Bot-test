# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T04:22:36.022997+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `13`; crypto_alt avg `0.0247` n `236`; crypto_major avg `-0.0238` n `8`; equity avg `-0.0616` n `151`; fx avg `-0.0011` n `6`; index avg `-0.0132` n `26`; metal avg `-0.0047` n `20`; unknown avg `-0.1265` n `1193`
- 1h: commodity avg `0.0002` n `13`; crypto_alt avg `0.2309` n `236`; crypto_major avg `0.0423` n `8`; equity avg `-0.0081` n `151`; fx avg `-0.0031` n `6`; index avg `0.0017` n `26`; metal avg `0.0097` n `20`; unknown avg `-0.2255` n `1185`
- 4h: commodity avg `-0.0601` n `13`; crypto_alt avg `0.0344` n `236`; crypto_major avg `-0.0115` n `8`; equity avg `0.1666` n `151`; fx avg `-0.0079` n `6`; index avg `0.0187` n `26`; metal avg `0.0108` n `20`; unknown avg `0.6245` n `1183`
- 24h: commodity avg `0.6161` n `13`; crypto_alt avg `-1.3159` n `236`; crypto_major avg `-1.0895` n `8`; equity avg `-4.282` n `151`; fx avg `-0.0637` n `6`; index avg `-0.6902` n `26`; metal avg `-0.2846` n `20`; unknown avg `40.5138` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1731`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1193`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.093`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0764`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
