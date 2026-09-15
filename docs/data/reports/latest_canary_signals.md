# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T11:07:26.286022+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0588` n `12`; crypto_alt avg `0.0362` n `233`; crypto_major avg `-0.0301` n `8`; equity avg `0.1287` n `136`; fx avg `-0.0076` n `6`; index avg `0.0185` n `27`; metal avg `-0.0149` n `20`; unknown avg `1.278` n `906`
- 1h: commodity avg `-0.1417` n `12`; crypto_alt avg `0.01` n `233`; crypto_major avg `0.1695` n `8`; equity avg `0.3404` n `136`; fx avg `-0.0085` n `6`; index avg `0.0702` n `27`; metal avg `0.0568` n `20`; unknown avg `1.9517` n `904`
- 4h: commodity avg `-0.2072` n `12`; crypto_alt avg `-0.1076` n `233`; crypto_major avg `0.1994` n `8`; equity avg `0.4166` n `136`; fx avg `0.0162` n `6`; index avg `0.0709` n `27`; metal avg `0.021` n `20`; unknown avg `1.1501` n `898`
- 24h: commodity avg `-0.1152` n `12`; crypto_alt avg `-1.0517` n `233`; crypto_major avg `-0.4737` n `8`; equity avg `0.4822` n `136`; fx avg `0.1818` n `6`; index avg `0.0533` n `27`; metal avg `0.0396` n `20`; unknown avg `-0.493` n `818`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
