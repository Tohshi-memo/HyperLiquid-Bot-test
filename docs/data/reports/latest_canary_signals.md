# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T18:26:19.013207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1504` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.4787` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0482` n `12`; crypto_alt avg `-0.4734` n `232`; crypto_major avg `-0.4155` n `8`; equity avg `-0.1278` n `131`; fx avg `-0.001` n `6`; index avg `-0.0137` n `26`; metal avg `-0.0162` n `20`; unknown avg `-0.1406` n `793`
- 1h: commodity avg `0.0446` n `12`; crypto_alt avg `-0.917` n `232`; crypto_major avg `-0.9207` n `8`; equity avg `-0.1677` n `131`; fx avg `0.0078` n `6`; index avg `-0.0344` n `26`; metal avg `-0.1001` n `20`; unknown avg `-0.8778` n `791`
- 4h: commodity avg `0.5293` n `12`; crypto_alt avg `-1.5698` n `232`; crypto_major avg `-1.6211` n `8`; equity avg `-0.3559` n `131`; fx avg `-0.0002` n `6`; index avg `-0.1424` n `26`; metal avg `-0.279` n `20`; unknown avg `-1.2971` n `790`
- 24h: commodity avg `0.6909` n `12`; crypto_alt avg `-0.9464` n `232`; crypto_major avg `-2.324` n `8`; equity avg `-1.6571` n `130`; fx avg `0.0409` n `6`; index avg `-0.2985` n `26`; metal avg `-0.7121` n `20`; unknown avg `-0.1905` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0383`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0374`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0373`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0356`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0353`, n `668`, weak_sample_signal
