# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T05:07:30.413760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `12`; crypto_alt avg `-0.0032` n `230`; crypto_major avg `0.015` n `8`; equity avg `-0.0151` n `92`; fx avg `0.0078` n `6`; index avg `0.0002` n `25`; metal avg `-0.0049` n `20`; unknown avg `-0.0743` n `765`
- 1h: commodity avg `-0.0554` n `12`; crypto_alt avg `-0.1901` n `229`; crypto_major avg `-0.0481` n `8`; equity avg `-0.0244` n `92`; fx avg `0.0074` n `6`; index avg `0.0064` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.1276` n `765`
- 4h: commodity avg `-0.1003` n `12`; crypto_alt avg `-0.0123` n `229`; crypto_major avg `-0.1044` n `8`; equity avg `-0.018` n `92`; fx avg `0.0097` n `6`; index avg `0.011` n `25`; metal avg `0.0177` n `20`; unknown avg `-0.2027` n `763`
- 24h: commodity avg `-0.4153` n `12`; crypto_alt avg `0.2392` n `229`; crypto_major avg `-0.2882` n `8`; equity avg `-0.6279` n `92`; fx avg `-0.1611` n `6`; index avg `0.0682` n `25`; metal avg `-0.0003` n `20`; unknown avg `4.1814` n `730`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
