# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T08:22:40.963894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1928` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.4617` n `230`; crypto_major avg `-0.5436` n `8`; equity avg `-0.073` n `94`; fx avg `-0.0011` n `6`; index avg `-0.003` n `25`; metal avg `0.0166` n `20`; unknown avg `-0.1652` n `768`
- 1h: commodity avg `0.0456` n `12`; crypto_alt avg `-0.9977` n `230`; crypto_major avg `-1.2863` n `8`; equity avg `-0.6023` n `94`; fx avg `-0.0029` n `6`; index avg `-0.0935` n `25`; metal avg `0.0165` n `20`; unknown avg `-0.1805` n `768`
- 4h: commodity avg `-0.0666` n `12`; crypto_alt avg `-1.1294` n `230`; crypto_major avg `-1.0934` n `8`; equity avg `-0.8356` n `94`; fx avg `-0.0838` n `6`; index avg `-0.1211` n `25`; metal avg `-0.1192` n `20`; unknown avg `-0.1055` n `752`
- 24h: commodity avg `-0.1958` n `12`; crypto_alt avg `-0.7253` n `230`; crypto_major avg `-0.8288` n `8`; equity avg `-2.6823` n `93`; fx avg `0.0258` n `6`; index avg `-0.4781` n `25`; metal avg `-0.0369` n `20`; unknown avg `-0.24` n `749`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1564`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
