# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T22:52:23.775316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `13`; crypto_alt avg `-0.1061` n `235`; crypto_major avg `-0.1032` n `8`; equity avg `-0.0715` n `151`; fx avg `-0.002` n `6`; index avg `-0.0185` n `26`; metal avg `-0.0097` n `20`; unknown avg `1.9836` n `1135`
- 1h: commodity avg `0.0715` n `13`; crypto_alt avg `-0.1071` n `235`; crypto_major avg `-0.1844` n `8`; equity avg `-0.0324` n `151`; fx avg `0.0019` n `6`; index avg `0.005` n `26`; metal avg `0.0165` n `20`; unknown avg `1.8291` n `1117`
- 4h: commodity avg `-0.0715` n `13`; crypto_alt avg `-1.0385` n `235`; crypto_major avg `-0.5105` n `8`; equity avg `0.0659` n `151`; fx avg `-0.0057` n `6`; index avg `0.0116` n `26`; metal avg `0.0544` n `20`; unknown avg `2.6642` n `1060`
- 24h: commodity avg `0.2817` n `13`; crypto_alt avg `-4.1931` n `235`; crypto_major avg `-2.5425` n `8`; equity avg `-3.5565` n `151`; fx avg `-0.1511` n `6`; index avg `-0.3445` n `26`; metal avg `-0.075` n `20`; unknown avg `0.0796` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2031`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1766`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1487`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1158`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0858`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0843`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0751`, n `666`, weak_sample_signal
