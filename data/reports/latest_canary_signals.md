# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T11:07:30.976376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0299` n `12`; crypto_alt avg `-0.2869` n `233`; crypto_major avg `-0.2788` n `8`; equity avg `-0.1306` n `136`; fx avg `-0.0024` n `6`; index avg `-0.0001` n `27`; metal avg `-0.001` n `20`; unknown avg `0.7555` n `892`
- 1h: commodity avg `0.0254` n `12`; crypto_alt avg `-0.5073` n `233`; crypto_major avg `-0.4997` n `8`; equity avg `0.0929` n `136`; fx avg `0.0115` n `6`; index avg `0.0505` n `27`; metal avg `0.0581` n `20`; unknown avg `0.7183` n `892`
- 4h: commodity avg `-0.0222` n `12`; crypto_alt avg `-0.5818` n `233`; crypto_major avg `-0.1354` n `8`; equity avg `-0.4359` n `136`; fx avg `0.0012` n `6`; index avg `-0.0403` n `27`; metal avg `-0.3049` n `20`; unknown avg `6.1438` n `886`
- 24h: commodity avg `0.5567` n `12`; crypto_alt avg `0.0492` n `233`; crypto_major avg `1.6115` n `8`; equity avg `-0.862` n `136`; fx avg `0.0403` n `6`; index avg `-0.2065` n `27`; metal avg `-0.4628` n `20`; unknown avg `1.0752` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
