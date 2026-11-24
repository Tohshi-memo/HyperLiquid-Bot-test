# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T17:07:27.826889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2704` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0371` n `13`; crypto_alt avg `0.1544` n `239`; crypto_major avg `0.1207` n `8`; equity avg `0.1643` n `168`; fx avg `0.0114` n `6`; index avg `0.0336` n `27`; metal avg `0.0053` n `20`; unknown avg `18.9357` n `1255`
- 1h: commodity avg `0.1739` n `13`; crypto_alt avg `0.2063` n `239`; crypto_major avg `0.23` n `8`; equity avg `0.767` n `168`; fx avg `0.0325` n `6`; index avg `0.1262` n `27`; metal avg `0.1112` n `20`; unknown avg `37.7625` n `1259`
- 4h: commodity avg `0.3145` n `13`; crypto_alt avg `-1.0499` n `239`; crypto_major avg `-1.3482` n `8`; equity avg `-1.8248` n `168`; fx avg `0.0325` n `6`; index avg `-0.0778` n `27`; metal avg `-0.619` n `20`; unknown avg `-0.2979` n `1241`
- 24h: commodity avg `0.3484` n `13`; crypto_alt avg `-4.632` n `239`; crypto_major avg `-4.4585` n `8`; equity avg `-4.6459` n `167`; fx avg `0.2617` n `6`; index avg `-0.3154` n `27`; metal avg `-1.2579` n `20`; unknown avg `-0.8339` n `1129`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
