# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T05:37:23.512060+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `13`; crypto_alt avg `0.0414` n `238`; crypto_major avg `0.0211` n `8`; equity avg `0.0033` n `156`; fx avg `0.0024` n `6`; index avg `0.0106` n `27`; metal avg `-0.0017` n `20`; unknown avg `-0.1424` n `1260`
- 1h: commodity avg `-0.0183` n `13`; crypto_alt avg `-0.4096` n `238`; crypto_major avg `-0.0085` n `8`; equity avg `0.0141` n `156`; fx avg `-0.005` n `6`; index avg `0.0112` n `27`; metal avg `0.0067` n `20`; unknown avg `-0.1886` n `1254`
- 4h: commodity avg `0.1235` n `13`; crypto_alt avg `-1.2424` n `238`; crypto_major avg `-0.7539` n `8`; equity avg `-0.0723` n `156`; fx avg `0.0014` n `6`; index avg `-0.046` n `27`; metal avg `-0.0111` n `20`; unknown avg `-0.3941` n `1230`
- 24h: commodity avg `-0.0083` n `13`; crypto_alt avg `0.3684` n `238`; crypto_major avg `-1.8819` n `8`; equity avg `-2.6556` n `156`; fx avg `-0.0813` n `6`; index avg `-0.1919` n `27`; metal avg `-0.739` n `20`; unknown avg `4.1422` n `1004`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
