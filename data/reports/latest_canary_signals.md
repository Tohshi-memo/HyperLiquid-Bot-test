# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T16:07:33.672271+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2001` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0632` n `12`; crypto_alt avg `-0.2316` n `230`; crypto_major avg `-0.3524` n `8`; equity avg `0.0464` n `100`; fx avg `0.0045` n `6`; index avg `0.0487` n `25`; metal avg `0.0132` n `20`; unknown avg `-0.1863` n `772`
- 1h: commodity avg `0.0532` n `12`; crypto_alt avg `-0.1912` n `230`; crypto_major avg `-0.2023` n `8`; equity avg `0.1131` n `100`; fx avg `-0.0002` n `6`; index avg `0.0203` n `25`; metal avg `-0.037` n `20`; unknown avg `-0.1577` n `772`
- 4h: commodity avg `0.2595` n `12`; crypto_alt avg `-0.8659` n `230`; crypto_major avg `-1.4695` n `8`; equity avg `-1.1449` n `99`; fx avg `-0.0226` n `6`; index avg `-0.2694` n `25`; metal avg `-0.3266` n `20`; unknown avg `0.0172` n `772`
- 24h: commodity avg `1.1549` n `12`; crypto_alt avg `-1.4957` n `230`; crypto_major avg `-1.9757` n `8`; equity avg `-2.1316` n `99`; fx avg `-0.0815` n `6`; index avg `-0.4219` n `25`; metal avg `-0.9398` n `20`; unknown avg `-0.3282` n `740`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
