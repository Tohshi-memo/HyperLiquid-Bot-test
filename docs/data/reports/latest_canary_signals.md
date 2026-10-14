# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T22:52:29.719849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `13`; crypto_alt avg `0.2682` n `236`; crypto_major avg `0.3022` n `8`; equity avg `0.2278` n `151`; fx avg `0.0354` n `6`; index avg `0.0128` n `26`; metal avg `0.0155` n `20`; unknown avg `1.0228` n `1136`
- 1h: commodity avg `-0.0275` n `13`; crypto_alt avg `0.1067` n `236`; crypto_major avg `-0.014` n `8`; equity avg `-0.5698` n `151`; fx avg `0.0368` n `6`; index avg `-0.0734` n `26`; metal avg `0.0374` n `20`; unknown avg `0.1002` n `1078`
- 4h: commodity avg `0.0909` n `13`; crypto_alt avg `0.4056` n `236`; crypto_major avg `0.1096` n `8`; equity avg `-1.0185` n `151`; fx avg `0.0549` n `6`; index avg `-0.1114` n `26`; metal avg `0.0655` n `20`; unknown avg `1.4182` n `998`
- 24h: commodity avg `-0.119` n `13`; crypto_alt avg `-2.2215` n `236`; crypto_major avg `-2.1108` n `8`; equity avg `-5.2791` n `151`; fx avg `-0.0975` n `6`; index avg `-0.7029` n `26`; metal avg `-0.8062` n `20`; unknown avg `1392.5673` n `890`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0884`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0863`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0834`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0529`, n `666`, weak_sample_signal
