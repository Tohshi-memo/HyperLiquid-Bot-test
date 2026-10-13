# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T08:26:23.558811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `13`; crypto_alt avg `-0.0749` n `235`; crypto_major avg `-0.0664` n `8`; equity avg `0.2511` n `151`; fx avg `-0.0073` n `6`; index avg `0.028` n `26`; metal avg `0.0365` n `20`; unknown avg `2.0229` n `1135`
- 1h: commodity avg `-0.0421` n `13`; crypto_alt avg `-0.1129` n `235`; crypto_major avg `0.1479` n `8`; equity avg `0.5279` n `151`; fx avg `0.0138` n `6`; index avg `0.0563` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.5025` n `1117`
- 4h: commodity avg `-0.0148` n `13`; crypto_alt avg `0.6356` n `235`; crypto_major avg `0.6203` n `8`; equity avg `0.4702` n `151`; fx avg `0.0303` n `6`; index avg `0.116` n `26`; metal avg `0.0881` n `20`; unknown avg `1.6152` n `1097`
- 24h: commodity avg `0.2379` n `13`; crypto_alt avg `-3.4772` n `235`; crypto_major avg `-1.7071` n `8`; equity avg `-2.9068` n `151`; fx avg `0.0783` n `6`; index avg `-0.4076` n `26`; metal avg `0.0876` n `20`; unknown avg `0.286` n `883`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1899`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1709`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1534`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1326`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0878`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0765`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0764`, n `666`, weak_sample_signal
