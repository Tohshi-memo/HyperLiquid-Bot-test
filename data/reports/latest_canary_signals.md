# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T08:07:29.579831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0149` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0332` n `13`; crypto_alt avg `0.1249` n `239`; crypto_major avg `0.0874` n `8`; equity avg `0.1791` n `168`; fx avg `0.0082` n `6`; index avg `0.0276` n `27`; metal avg `-0.0217` n `20`; unknown avg `0.6523` n `1237`
- 1h: commodity avg `-0.1371` n `13`; crypto_alt avg `-0.4374` n `239`; crypto_major avg `-1.075` n `8`; equity avg `-0.5894` n `168`; fx avg `-0.0144` n `6`; index avg `-0.0601` n `27`; metal avg `-0.0855` n `20`; unknown avg `2.3624` n `1239`
- 4h: commodity avg `-0.2642` n `13`; crypto_alt avg `0.4745` n `239`; crypto_major avg `-0.719` n `8`; equity avg `-1.2348` n `168`; fx avg `-0.0523` n `6`; index avg `-0.1079` n `27`; metal avg `-0.2251` n `20`; unknown avg `374.6627` n `1207`
- 24h: commodity avg `-0.0073` n `13`; crypto_alt avg `-2.8684` n `239`; crypto_major avg `-3.2837` n `8`; equity avg `-5.833` n `167`; fx avg `0.0759` n `6`; index avg `-0.544` n `27`; metal avg `-1.0613` n `20`; unknown avg `838.964` n `1035`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
