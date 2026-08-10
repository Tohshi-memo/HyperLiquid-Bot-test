# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T16:52:33.827872+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0138` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0123` n `12`; crypto_alt avg `-0.1272` n `230`; crypto_major avg `-0.2078` n `8`; equity avg `-0.0824` n `113`; fx avg `-0.0118` n `6`; index avg `-0.0208` n `25`; metal avg `-0.0586` n `20`; unknown avg `0.0196` n `785`
- 1h: commodity avg `0.0041` n `12`; crypto_alt avg `-0.1631` n `230`; crypto_major avg `-0.3465` n `8`; equity avg `-0.2789` n `113`; fx avg `-0.0176` n `6`; index avg `-0.0403` n `25`; metal avg `-0.0177` n `20`; unknown avg `-0.027` n `785`
- 4h: commodity avg `0.4082` n `12`; crypto_alt avg `-0.7145` n `230`; crypto_major avg `-1.0096` n `8`; equity avg `-0.2938` n `113`; fx avg `0.0258` n `6`; index avg `0.0042` n `25`; metal avg `0.1228` n `20`; unknown avg `1.642` n `784`
- 24h: commodity avg `1.176` n `12`; crypto_alt avg `-0.8461` n `230`; crypto_major avg `-1.7196` n `8`; equity avg `-1.335` n `113`; fx avg `0.2331` n `6`; index avg `-0.0671` n `25`; metal avg `-0.053` n `20`; unknown avg `103.3406` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
