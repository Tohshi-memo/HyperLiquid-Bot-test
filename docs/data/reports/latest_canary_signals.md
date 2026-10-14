# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T16:07:31.863595+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1946` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9323` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5448` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0772` n `13`; crypto_alt avg `0.1397` n `235`; crypto_major avg `0.0956` n `8`; equity avg `-0.0705` n `151`; fx avg `0.0054` n `6`; index avg `-0.0124` n `26`; metal avg `-0.0195` n `20`; unknown avg `0.1552` n `1129`
- 1h: commodity avg `0.0021` n `13`; crypto_alt avg `0.0985` n `235`; crypto_major avg `0.1649` n `8`; equity avg `-0.4309` n `151`; fx avg `0.0081` n `6`; index avg `-0.0745` n `26`; metal avg `-0.0812` n `20`; unknown avg `-0.1984` n `1105`
- 4h: commodity avg `-0.1446` n `13`; crypto_alt avg `-2.6868` n `235`; crypto_major avg `-2.3392` n `8`; equity avg `-2.7595` n `151`; fx avg `-0.1295` n `6`; index avg `-0.4069` n `26`; metal avg `-0.7944` n `20`; unknown avg `3.0485` n `1102`
- 24h: commodity avg `0.0896` n `13`; crypto_alt avg `-2.6129` n `235`; crypto_major avg `-2.1728` n `8`; equity avg `-2.9314` n `151`; fx avg `-0.1442` n `6`; index avg `-0.3736` n `26`; metal avg `-0.8198` n `20`; unknown avg `1260.7204` n `981`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0925`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0805`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0727`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0651`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0524`, n `666`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0519`, n `666`, weak_sample_signal
