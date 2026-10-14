# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T08:07:27.896160+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0196` n `13`; crypto_alt avg `0.6974` n `235`; crypto_major avg `0.6011` n `8`; equity avg `0.1035` n `151`; fx avg `0.0056` n `6`; index avg `0.0161` n `26`; metal avg `0.0564` n `20`; unknown avg `0.9308` n `1117`
- 1h: commodity avg `-0.0903` n `13`; crypto_alt avg `0.5155` n `235`; crypto_major avg `0.4616` n `8`; equity avg `-0.0087` n `151`; fx avg `-0.0047` n `6`; index avg `-0.0055` n `26`; metal avg `0.0346` n `20`; unknown avg `0.5865` n `1117`
- 4h: commodity avg `-0.0976` n `13`; crypto_alt avg `0.2165` n `235`; crypto_major avg `0.3818` n `8`; equity avg `-0.6366` n `151`; fx avg `-0.0374` n `6`; index avg `-0.0944` n `26`; metal avg `-0.0464` n `20`; unknown avg `0.8773` n `1101`
- 24h: commodity avg `1.0007` n `13`; crypto_alt avg `-0.4018` n `235`; crypto_major avg `-0.1843` n `8`; equity avg `-0.1451` n `151`; fx avg `-0.0164` n `6`; index avg `0.0117` n `26`; metal avg `-0.4142` n `20`; unknown avg `0.9617` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1548`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1348`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1135`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0711`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0701`, n `666`, weak_sample_signal
