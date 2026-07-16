# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T17:52:26.980807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0666` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0797` n `12`; crypto_alt avg `-0.2213` n `230`; crypto_major avg `-0.2669` n `8`; equity avg `-0.236` n `94`; fx avg `0.0101` n `6`; index avg `-0.019` n `25`; metal avg `0.0029` n `20`; unknown avg `-0.1854` n `768`
- 1h: commodity avg `-0.1238` n `12`; crypto_alt avg `-0.5456` n `230`; crypto_major avg `-0.8864` n `8`; equity avg `-0.442` n `94`; fx avg `-0.0054` n `6`; index avg `-0.0566` n `25`; metal avg `-0.159` n `20`; unknown avg `-0.3206` n `768`
- 4h: commodity avg `-0.5245` n `12`; crypto_alt avg `-0.475` n `230`; crypto_major avg `-1.1426` n `8`; equity avg `-1.1752` n `94`; fx avg `-0.0593` n `6`; index avg `-0.076` n `25`; metal avg `-0.1997` n `20`; unknown avg `-0.3663` n `768`
- 24h: commodity avg `-0.2897` n `12`; crypto_alt avg `-1.1404` n `230`; crypto_major avg `-2.4712` n `8`; equity avg `-3.7137` n `94`; fx avg `-0.1515` n `6`; index avg `-0.4489` n `25`; metal avg `-0.6258` n `20`; unknown avg `-0.3565` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
