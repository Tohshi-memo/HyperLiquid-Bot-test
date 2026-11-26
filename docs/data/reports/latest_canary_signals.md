# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T01:22:37.778859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0176` n `13`; crypto_alt avg `0.2485` n `239`; crypto_major avg `0.2634` n `8`; equity avg `0.2707` n `168`; fx avg `0.0016` n `6`; index avg `0.032` n `27`; metal avg `0.2066` n `20`; unknown avg `158.1844` n `1265`
- 1h: commodity avg `0.0841` n `13`; crypto_alt avg `0.0817` n `239`; crypto_major avg `-0.1606` n `8`; equity avg `0.2155` n `168`; fx avg `0.0073` n `6`; index avg `0.0369` n `27`; metal avg `0.1029` n `20`; unknown avg `158.6159` n `1263`
- 4h: commodity avg `0.0913` n `13`; crypto_alt avg `1.1036` n `239`; crypto_major avg `0.542` n `8`; equity avg `1.4351` n `168`; fx avg `-0.0307` n `6`; index avg `0.1445` n `27`; metal avg `0.2526` n `20`; unknown avg `44.6057` n `1185`
- 24h: commodity avg `0.5295` n `13`; crypto_alt avg `3.7471` n `239`; crypto_major avg `2.4392` n `8`; equity avg `1.4882` n `168`; fx avg `0.0124` n `6`; index avg `0.1384` n `27`; metal avg `0.5736` n `20`; unknown avg `768.9367` n `1019`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1903`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
