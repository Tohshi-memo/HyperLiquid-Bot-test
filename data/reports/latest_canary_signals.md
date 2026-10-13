# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T18:52:32.830989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0273` n `13`; crypto_alt avg `0.3229` n `235`; crypto_major avg `0.3025` n `8`; equity avg `-0.0005` n `151`; fx avg `0.0045` n `6`; index avg `-0.0032` n `26`; metal avg `0.0273` n `20`; unknown avg `-0.4093` n `1135`
- 1h: commodity avg `0.0254` n `13`; crypto_alt avg `0.4976` n `235`; crypto_major avg `0.4687` n `8`; equity avg `0.2403` n `151`; fx avg `0.0164` n `6`; index avg `0.0524` n `26`; metal avg `0.1409` n `20`; unknown avg `0.3047` n `1133`
- 4h: commodity avg `0.2597` n `13`; crypto_alt avg `-0.1285` n `235`; crypto_major avg `-0.2224` n `8`; equity avg `0.3607` n `151`; fx avg `0.0166` n `6`; index avg `0.0486` n `26`; metal avg `-0.0829` n `20`; unknown avg `0.4268` n `1123`
- 24h: commodity avg `0.562` n `13`; crypto_alt avg `-1.2924` n `235`; crypto_major avg `-0.0536` n `8`; equity avg `-0.7968` n `151`; fx avg `0.178` n `6`; index avg `-0.1592` n `26`; metal avg `-0.2022` n `20`; unknown avg `0.1074` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1621`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1458`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.121`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0919`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0877`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
