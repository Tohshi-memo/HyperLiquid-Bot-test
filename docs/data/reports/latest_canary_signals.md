# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T13:22:33.329299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1051` n `12`; crypto_alt avg `-0.0571` n `233`; crypto_major avg `-0.2086` n `8`; equity avg `-0.1539` n `136`; fx avg `0.0126` n `6`; index avg `-0.0232` n `27`; metal avg `0.015` n `20`; unknown avg `0.1216` n `908`
- 1h: commodity avg `-0.0197` n `12`; crypto_alt avg `0.1989` n `233`; crypto_major avg `0.2677` n `8`; equity avg `-0.1258` n `136`; fx avg `-0.0056` n `6`; index avg `-0.0066` n `27`; metal avg `0.164` n `20`; unknown avg `2.9656` n `900`
- 4h: commodity avg `-0.1308` n `12`; crypto_alt avg `0.4254` n `233`; crypto_major avg `0.568` n `8`; equity avg `0.5523` n `136`; fx avg `-0.0208` n `6`; index avg `0.1731` n `27`; metal avg `0.3276` n `20`; unknown avg `2.3886` n `898`
- 24h: commodity avg `-0.0992` n `12`; crypto_alt avg `-0.4131` n `233`; crypto_major avg `-0.1037` n `8`; equity avg `0.7352` n `136`; fx avg `0.1619` n `6`; index avg `0.1146` n `27`; metal avg `0.1547` n `20`; unknown avg `-0.4259` n `818`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
