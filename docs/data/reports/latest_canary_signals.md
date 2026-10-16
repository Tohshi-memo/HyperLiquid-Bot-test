# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T16:52:33.894809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1072` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0273` n `13`; crypto_alt avg `-0.6698` n `236`; crypto_major avg `-0.448` n `8`; equity avg `-0.2344` n `151`; fx avg `0.0052` n `6`; index avg `-0.0464` n `26`; metal avg `-0.0282` n `20`; unknown avg `0.7549` n `1174`
- 1h: commodity avg `0.5138` n `13`; crypto_alt avg `-0.5765` n `236`; crypto_major avg `-0.2167` n `8`; equity avg `-0.4247` n `151`; fx avg `-0.0034` n `6`; index avg `-0.115` n `26`; metal avg `-0.0915` n `20`; unknown avg `0.1156` n `1164`
- 4h: commodity avg `0.5179` n `13`; crypto_alt avg `-1.8676` n `236`; crypto_major avg `-1.4802` n `8`; equity avg `-2.2447` n `151`; fx avg `0.0124` n `6`; index avg `-0.373` n `26`; metal avg `-0.1858` n `20`; unknown avg `0.8297` n `996`
- 24h: commodity avg `0.2082` n `13`; crypto_alt avg `-1.293` n `236`; crypto_major avg `-1.2425` n `8`; equity avg `-1.3424` n `151`; fx avg `0.0012` n `6`; index avg `-0.292` n `26`; metal avg `0.0411` n `20`; unknown avg `-0.3054` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1253`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0917`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0913`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0816`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0779`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0731`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
