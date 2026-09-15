# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T12:52:32.736573+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1162` n `12`; crypto_alt avg `0.208` n `233`; crypto_major avg `0.2728` n `8`; equity avg `0.1259` n `136`; fx avg `-0.014` n `6`; index avg `0.0305` n `27`; metal avg `0.1083` n `20`; unknown avg `3.9225` n `908`
- 1h: commodity avg `0.0117` n `12`; crypto_alt avg `0.6471` n `233`; crypto_major avg `0.5167` n `8`; equity avg `0.0763` n `136`; fx avg `0.0037` n `6`; index avg `0.0272` n `27`; metal avg `0.1055` n `20`; unknown avg `4.1567` n `900`
- 4h: commodity avg `-0.245` n `12`; crypto_alt avg `0.3326` n `233`; crypto_major avg `0.6442` n `8`; equity avg `0.7116` n `136`; fx avg `-0.0455` n `6`; index avg `0.1875` n `27`; metal avg `0.3258` n `20`; unknown avg `7.3294` n `898`
- 24h: commodity avg `-0.2756` n `12`; crypto_alt avg `-0.5544` n `233`; crypto_major avg `-0.2232` n `8`; equity avg `0.9656` n `136`; fx avg `0.152` n `6`; index avg `0.1631` n `27`; metal avg `0.1997` n `20`; unknown avg `-0.4363` n `818`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
