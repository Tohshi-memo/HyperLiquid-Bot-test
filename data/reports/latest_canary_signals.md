# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T13:52:30.489765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.83` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.8225` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.6897` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0688` n `12`; crypto_alt avg `0.4756` n `232`; crypto_major avg `0.2145` n `8`; equity avg `0.2155` n `133`; fx avg `0.014` n `6`; index avg `0.0359` n `26`; metal avg `0.0478` n `20`; unknown avg `1.4675` n `791`
- 1h: commodity avg `-0.2557` n `12`; crypto_alt avg `0.6008` n `232`; crypto_major avg `0.108` n `8`; equity avg `1.0249` n `133`; fx avg `0.0449` n `6`; index avg `0.1636` n `26`; metal avg `0.1478` n `20`; unknown avg `14.2435` n `747`
- 4h: commodity avg `-0.2777` n `12`; crypto_alt avg `-1.2638` n `232`; crypto_major avg `-1.6335` n `8`; equity avg `0.189` n `133`; fx avg `-0.1689` n `6`; index avg `0.0562` n `26`; metal avg `-0.1552` n `20`; unknown avg `1.2683` n `741`
- 24h: commodity avg `-0.632` n `12`; crypto_alt avg `1.1703` n `232`; crypto_major avg `1.2276` n `8`; equity avg `2.0247` n `133`; fx avg `-0.0972` n `6`; index avg `0.3034` n `26`; metal avg `0.0885` n `20`; unknown avg `1.4467` n `702`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
