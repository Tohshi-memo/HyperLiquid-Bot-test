# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T07:52:25.302644+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0302` n `13`; crypto_alt avg `-0.0243` n `235`; crypto_major avg `0.0311` n `8`; equity avg `0.1749` n `151`; fx avg `0.0122` n `6`; index avg `0.0443` n `26`; metal avg `-0.0128` n `20`; unknown avg `4.0278` n `1135`
- 1h: commodity avg `-0.0735` n `13`; crypto_alt avg `-0.1688` n `235`; crypto_major avg `0.0525` n `8`; equity avg `0.1142` n `151`; fx avg `0.0374` n `6`; index avg `0.0383` n `26`; metal avg `0.0265` n `20`; unknown avg `3.8631` n `1133`
- 4h: commodity avg `-0.1499` n `13`; crypto_alt avg `0.9969` n `235`; crypto_major avg `0.6971` n `8`; equity avg `0.1045` n `151`; fx avg `0.0284` n `6`; index avg `0.0918` n `26`; metal avg `0.0764` n `20`; unknown avg `2.1494` n `1107`
- 24h: commodity avg `0.2605` n `13`; crypto_alt avg `-3.6515` n `235`; crypto_major avg `-2.1037` n `8`; equity avg `-3.4873` n `151`; fx avg `0.0855` n `6`; index avg `-0.4521` n `26`; metal avg `-0.0453` n `20`; unknown avg `0.5696` n `855`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.196`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1766`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1546`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1331`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0875`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0808`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `666`, weak_sample_signal
