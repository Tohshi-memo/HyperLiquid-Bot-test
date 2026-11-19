# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T21:52:27.607365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.719` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.3218` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0056` n `13`; crypto_alt avg `0.182` n `239`; crypto_major avg `0.1963` n `8`; equity avg `0.206` n `165`; fx avg `0.0155` n `6`; index avg `0.0166` n `27`; metal avg `0.0373` n `20`; unknown avg `0.6101` n `1262`
- 1h: commodity avg `0.022` n `13`; crypto_alt avg `-0.5092` n `239`; crypto_major avg `-0.9069` n `8`; equity avg `-1.9457` n `165`; fx avg `-0.0063` n `6`; index avg `-0.1074` n `27`; metal avg `-0.341` n `20`; unknown avg `0.8184` n `1240`
- 4h: commodity avg `-0.0791` n `13`; crypto_alt avg `-0.7738` n `239`; crypto_major avg `-1.5704` n `8`; equity avg `-3.2894` n `165`; fx avg `-0.0237` n `6`; index avg `-0.2486` n `27`; metal avg `-0.4541` n `20`; unknown avg `1.882` n `1234`
- 24h: commodity avg `0.0472` n `13`; crypto_alt avg `-0.8152` n `239`; crypto_major avg `-0.5216` n `8`; equity avg `-3.3561` n `165`; fx avg `-0.0082` n `6`; index avg `-0.1965` n `27`; metal avg `-0.8473` n `20`; unknown avg `6.5666` n `1168`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.058`, n `668`, weak_sample_signal
