# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T11:07:31.321400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0809` n `13`; crypto_alt avg `-0.1375` n `237`; crypto_major avg `-0.1711` n `8`; equity avg `-0.3118` n `151`; fx avg `0.0203` n `6`; index avg `-0.054` n `26`; metal avg `0.0593` n `20`; unknown avg `-0.0758` n `1193`
- 1h: commodity avg `0.0862` n `13`; crypto_alt avg `-0.7615` n `237`; crypto_major avg `-0.6945` n `8`; equity avg `-0.0462` n `151`; fx avg `0.0162` n `6`; index avg `-0.0076` n `26`; metal avg `0.0444` n `20`; unknown avg `1.5797` n `1193`
- 4h: commodity avg `0.4557` n `13`; crypto_alt avg `-0.9213` n `237`; crypto_major avg `-0.8528` n `8`; equity avg `-0.1421` n `151`; fx avg `0.0164` n `6`; index avg `-0.0443` n `26`; metal avg `-0.0315` n `20`; unknown avg `0.3364` n `1146`
- 24h: commodity avg `-0.0359` n `13`; crypto_alt avg `-0.6123` n `237`; crypto_major avg `0.1092` n `8`; equity avg `2.4372` n `151`; fx avg `-0.0257` n `6`; index avg `0.4325` n `26`; metal avg `0.278` n `20`; unknown avg `1.1678` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1993`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1463`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.133`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0606`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
