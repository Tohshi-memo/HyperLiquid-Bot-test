# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T20:37:27.591823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `13`; crypto_alt avg `0.0315` n `236`; crypto_major avg `0.0246` n `8`; equity avg `-0.0186` n `151`; fx avg `0.0034` n `6`; index avg `-0.0102` n `26`; metal avg `0.0009` n `20`; unknown avg `2.8932` n `1193`
- 1h: commodity avg `-0.0604` n `13`; crypto_alt avg `-0.0086` n `236`; crypto_major avg `0.1294` n `8`; equity avg `-0.0467` n `151`; fx avg `0.0` n `6`; index avg `-0.0062` n `26`; metal avg `-0.0021` n `20`; unknown avg `1.1371` n `1177`
- 4h: commodity avg `-0.035` n `13`; crypto_alt avg `0.8567` n `236`; crypto_major avg `0.6232` n `8`; equity avg `0.1026` n `151`; fx avg `-0.0082` n `6`; index avg `-0.0003` n `26`; metal avg `0.0172` n `20`; unknown avg `4.9307` n `1113`
- 24h: commodity avg `0.0172` n `13`; crypto_alt avg `-1.0414` n `236`; crypto_major avg `-0.1344` n `8`; equity avg `-0.2268` n `151`; fx avg `-0.0289` n `6`; index avg `-0.0297` n `26`; metal avg `-0.0298` n `20`; unknown avg `5.8895` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1711`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1483`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1141`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1129`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0726`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
