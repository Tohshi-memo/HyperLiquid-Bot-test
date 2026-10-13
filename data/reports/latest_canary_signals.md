# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T07:07:29.580031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `13`; crypto_alt avg `-0.3269` n `235`; crypto_major avg `-0.2782` n `8`; equity avg `-0.1562` n `151`; fx avg `0.0061` n `6`; index avg `-0.0205` n `26`; metal avg `-0.006` n `20`; unknown avg `1.1049` n `1133`
- 1h: commodity avg `-0.0322` n `13`; crypto_alt avg `0.1017` n `235`; crypto_major avg `0.0098` n `8`; equity avg `-0.1739` n `151`; fx avg `-0.022` n `6`; index avg `0.0239` n `26`; metal avg `-0.0214` n `20`; unknown avg `0.0348` n `1133`
- 4h: commodity avg `0.0148` n `13`; crypto_alt avg `1.5995` n `235`; crypto_major avg `0.812` n `8`; equity avg `0.2981` n `151`; fx avg `-0.0021` n `6`; index avg `0.0876` n `26`; metal avg `0.1405` n `20`; unknown avg `1.0467` n `1075`
- 24h: commodity avg `0.4088` n `13`; crypto_alt avg `-3.7644` n `235`; crypto_major avg `-2.4947` n `8`; equity avg `-3.6297` n `151`; fx avg `0.0307` n `6`; index avg `-0.4736` n `26`; metal avg `-0.0749` n `20`; unknown avg `0.5123` n `855`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1964`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1787`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1552`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1326`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0887`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.082`, n `666`, weak_sample_signal
