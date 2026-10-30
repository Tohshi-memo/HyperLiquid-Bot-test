# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T08:52:31.070320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0012` n `13`; crypto_alt avg `-0.1668` n `238`; crypto_major avg `-0.1422` n `8`; equity avg `0.1127` n `156`; fx avg `0.0051` n `6`; index avg `0.0215` n `27`; metal avg `0.0825` n `20`; unknown avg `0.3565` n `1261`
- 1h: commodity avg `-0.0252` n `13`; crypto_alt avg `0.0164` n `238`; crypto_major avg `-0.037` n `8`; equity avg `-0.1214` n `156`; fx avg `0.0005` n `6`; index avg `-0.0064` n `27`; metal avg `0.145` n `20`; unknown avg `23.4907` n `1190`
- 4h: commodity avg `0.1961` n `13`; crypto_alt avg `0.053` n `238`; crypto_major avg `-0.6831` n `8`; equity avg `-0.9266` n `156`; fx avg `-0.0046` n `6`; index avg `-0.0353` n `27`; metal avg `-0.1348` n `20`; unknown avg `1.2506` n `1172`
- 24h: commodity avg `0.1134` n `13`; crypto_alt avg `-3.1522` n `238`; crypto_major avg `-0.5677` n `8`; equity avg `-2.85` n `155`; fx avg `0.1128` n `6`; index avg `-0.2567` n `27`; metal avg `-0.5466` n `20`; unknown avg `29.8819` n `938`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
