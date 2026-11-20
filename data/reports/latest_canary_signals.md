# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T14:52:25.246859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7191` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5492` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0504` n `13`; crypto_alt avg `-0.3859` n `239`; crypto_major avg `-0.6311` n `8`; equity avg `0.009` n `165`; fx avg `-0.0047` n `6`; index avg `-0.0041` n `27`; metal avg `-0.0587` n `20`; unknown avg `0.9833` n `1262`
- 1h: commodity avg `-0.3048` n `13`; crypto_alt avg `-0.4526` n `239`; crypto_major avg `-0.6592` n `8`; equity avg `0.3051` n `165`; fx avg `-0.0141` n `6`; index avg `0.0591` n `27`; metal avg `-0.0525` n `20`; unknown avg `3.2098` n `1258`
- 4h: commodity avg `0.1196` n `13`; crypto_alt avg `-1.5341` n `239`; crypto_major avg `-1.7484` n `8`; equity avg `-0.4914` n `165`; fx avg `0.0326` n `6`; index avg `-0.0293` n `27`; metal avg `-0.1992` n `20`; unknown avg `165.9948` n `1254`
- 24h: commodity avg `-0.6415` n `13`; crypto_alt avg `-4.8269` n `239`; crypto_major avg `-4.8438` n `8`; equity avg `-8.4175` n `165`; fx avg `-0.0392` n `6`; index avg `-0.7688` n `27`; metal avg `-1.2251` n `20`; unknown avg `39.1996` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
