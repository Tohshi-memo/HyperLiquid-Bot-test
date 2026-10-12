# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T21:37:30.446347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0062` n `13`; crypto_alt avg `-0.1798` n `235`; crypto_major avg `-0.0813` n `8`; equity avg `-0.0223` n `151`; fx avg `0.0003` n `6`; index avg `-0.0197` n `26`; metal avg `-0.0015` n `20`; unknown avg `-0.0838` n `1113`
- 1h: commodity avg `0.0478` n `13`; crypto_alt avg `-0.4152` n `235`; crypto_major avg `-0.2784` n `8`; equity avg `-0.0418` n `151`; fx avg `-0.0047` n `6`; index avg `0.0029` n `26`; metal avg `0.0359` n `20`; unknown avg `0.9787` n `1102`
- 4h: commodity avg `-0.1451` n `13`; crypto_alt avg `0.1046` n `235`; crypto_major avg `0.3263` n `8`; equity avg `0.0785` n `151`; fx avg `-0.0169` n `6`; index avg `-0.0114` n `26`; metal avg `0.0425` n `20`; unknown avg `0.9131` n `1076`
- 24h: commodity avg `0.2132` n `13`; crypto_alt avg `-2.739` n `235`; crypto_major avg `-1.4543` n `8`; equity avg `-3.3767` n `151`; fx avg `-0.1649` n `6`; index avg `-0.3402` n `26`; metal avg `-0.1114` n `20`; unknown avg `0.337` n `869`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2054`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1787`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1201`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1042`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1022`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.094`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0882`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0764`, n `666`, weak_sample_signal
