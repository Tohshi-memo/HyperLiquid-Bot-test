# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T16:22:39.464492+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4904` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0447` n `12`; crypto_alt avg `-0.1693` n `230`; crypto_major avg `-0.1922` n `8`; equity avg `0.2435` n `100`; fx avg `0.0035` n `6`; index avg `0.0241` n `25`; metal avg `-0.0092` n `20`; unknown avg `-0.0637` n `772`
- 1h: commodity avg `-0.1458` n `12`; crypto_alt avg `0.0077` n `230`; crypto_major avg `-0.1021` n `8`; equity avg `0.8698` n `100`; fx avg `0.0188` n `6`; index avg `0.1515` n `25`; metal avg `0.081` n `20`; unknown avg `-0.0734` n `772`
- 4h: commodity avg `0.0785` n `12`; crypto_alt avg `-0.9893` n `230`; crypto_major avg `-1.6387` n `8`; equity avg `-0.4094` n `99`; fx avg `-0.007` n `6`; index avg `-0.1483` n `25`; metal avg `-0.2342` n `20`; unknown avg `-0.0112` n `772`
- 24h: commodity avg `1.0423` n `12`; crypto_alt avg `-1.4286` n `230`; crypto_major avg `-1.889` n `8`; equity avg `-1.5384` n `99`; fx avg `-0.0713` n `6`; index avg `-0.3633` n `25`; metal avg `-0.8693` n `20`; unknown avg `-0.3503` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
