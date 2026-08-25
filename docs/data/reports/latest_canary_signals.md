# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T09:22:29.007474+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0927` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0636` n `12`; crypto_alt avg `0.2331` n `231`; crypto_major avg `0.2224` n `8`; equity avg `0.0773` n `122`; fx avg `0.0057` n `6`; index avg `0.0055` n `25`; metal avg `0.0619` n `20`; unknown avg `0.1241` n `794`
- 1h: commodity avg `-0.3652` n `12`; crypto_alt avg `-0.0359` n `231`; crypto_major avg `-0.1209` n `8`; equity avg `0.3668` n `122`; fx avg `-0.0089` n `6`; index avg `0.0875` n `25`; metal avg `-0.0218` n `20`; unknown avg `0.1061` n `794`
- 4h: commodity avg `-0.4602` n `12`; crypto_alt avg `-1.1419` n `231`; crypto_major avg `-0.9749` n `8`; equity avg `0.4066` n `122`; fx avg `0.0524` n `6`; index avg `0.1178` n `25`; metal avg `-0.1376` n `20`; unknown avg `-0.2689` n `778`
- 24h: commodity avg `-0.6473` n `12`; crypto_alt avg `0.9154` n `231`; crypto_major avg `2.1591` n `8`; equity avg `0.5829` n `122`; fx avg `0.0573` n `6`; index avg `0.1081` n `25`; metal avg `-0.1963` n `20`; unknown avg `0.0734` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
