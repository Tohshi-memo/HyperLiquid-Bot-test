# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T22:52:25.148681+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0622` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0143` n `12`; crypto_alt avg `0.0663` n `231`; crypto_major avg `0.0729` n `8`; equity avg `0.0197` n `122`; fx avg `-0.0002` n `6`; index avg `-0.0056` n `25`; metal avg `0.0137` n `20`; unknown avg `0.0` n `795`
- 1h: commodity avg `-0.0123` n `12`; crypto_alt avg `0.5995` n `231`; crypto_major avg `0.4693` n `8`; equity avg `0.0591` n `122`; fx avg `0.0022` n `6`; index avg `-0.0039` n `25`; metal avg `0.0975` n `20`; unknown avg `0.0376` n `795`
- 4h: commodity avg `-0.2293` n `12`; crypto_alt avg `-1.1548` n `231`; crypto_major avg `-1.0419` n `8`; equity avg `0.1032` n `122`; fx avg `-0.0064` n `6`; index avg `0.0203` n `25`; metal avg `0.1364` n `20`; unknown avg `-0.3256` n `795`
- 24h: commodity avg `-0.7092` n `12`; crypto_alt avg `-1.6601` n `231`; crypto_major avg `-0.544` n `8`; equity avg `2.1477` n `122`; fx avg `0.0602` n `6`; index avg `0.2531` n `25`; metal avg `-0.0424` n `20`; unknown avg `-0.5046` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
