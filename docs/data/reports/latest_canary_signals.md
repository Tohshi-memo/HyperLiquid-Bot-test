# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T19:09:48.980486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1247` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0526` n `12`; crypto_alt avg `-0.3513` n `230`; crypto_major avg `-0.0619` n `8`; equity avg `-0.0159` n `121`; fx avg `-0.0036` n `6`; index avg `0.0029` n `25`; metal avg `-0.0248` n `20`; unknown avg `1.0227` n `793`
- 1h: commodity avg `-0.0889` n `12`; crypto_alt avg `-1.3333` n `230`; crypto_major avg `-0.8566` n `8`; equity avg `-0.0269` n `121`; fx avg `-0.0064` n `6`; index avg `0.0042` n `25`; metal avg `-0.0286` n `20`; unknown avg `1.1548` n `793`
- 4h: commodity avg `0.069` n `12`; crypto_alt avg `-1.34` n `230`; crypto_major avg `-1.1148` n `8`; equity avg `0.0861` n `121`; fx avg `0.0373` n `6`; index avg `0.0099` n `25`; metal avg `0.0927` n `20`; unknown avg `1.185` n `793`
- 24h: commodity avg `0.1032` n `12`; crypto_alt avg `6.5265` n `230`; crypto_major avg `4.691` n `8`; equity avg `1.217` n `121`; fx avg `-0.0961` n `6`; index avg `0.1229` n `25`; metal avg `0.5974` n `20`; unknown avg `2.2354` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
