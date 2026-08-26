# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T22:21:27.007273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7173` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0144` n `12`; crypto_alt avg `0.3969` n `231`; crypto_major avg `0.7078` n `8`; equity avg `0.1299` n `124`; fx avg `0.0019` n `6`; index avg `0.0204` n `25`; metal avg `0.0598` n `20`; unknown avg `-0.0114` n `795`
- 1h: commodity avg `-0.025` n `12`; crypto_alt avg `0.9142` n `231`; crypto_major avg `1.1465` n `8`; equity avg `0.411` n `124`; fx avg `0.0042` n `6`; index avg `0.1235` n `25`; metal avg `0.1332` n `20`; unknown avg `0.1236` n `795`
- 4h: commodity avg `0.0157` n `12`; crypto_alt avg `1.7331` n `231`; crypto_major avg `1.8386` n `8`; equity avg `1.7909` n `124`; fx avg `-0.0182` n `6`; index avg `0.3178` n `25`; metal avg `0.1213` n `20`; unknown avg `0.436` n `795`
- 24h: commodity avg `0.3175` n `12`; crypto_alt avg `1.1113` n `231`; crypto_major avg `1.2408` n `8`; equity avg `1.4448` n `124`; fx avg `-0.0636` n `6`; index avg `0.2932` n `25`; metal avg `-0.2849` n `20`; unknown avg `0.9791` n `777`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
