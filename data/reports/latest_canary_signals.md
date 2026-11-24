# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T11:07:31.621285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.184` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0053` n `13`; crypto_alt avg `0.1769` n `239`; crypto_major avg `0.327` n `8`; equity avg `0.1833` n `166`; fx avg `-0.003` n `6`; index avg `0.0254` n `27`; metal avg `0.0611` n `20`; unknown avg `0.5124` n `1256`
- 1h: commodity avg `-0.0322` n `13`; crypto_alt avg `-0.3061` n `239`; crypto_major avg `-0.3901` n `8`; equity avg `-0.6414` n `166`; fx avg `-0.0209` n `6`; index avg `-0.0904` n `27`; metal avg `0.0185` n `20`; unknown avg `299.2661` n `1240`
- 4h: commodity avg `0.1879` n `13`; crypto_alt avg `-2.0012` n `239`; crypto_major avg `-1.5407` n `8`; equity avg `-2.8015` n `166`; fx avg `0.0949` n `6`; index avg `-0.3567` n `27`; metal avg `-0.1714` n `20`; unknown avg `334.2565` n `1198`
- 24h: commodity avg `-0.4702` n `13`; crypto_alt avg `-1.3404` n `239`; crypto_major avg `-1.6639` n `8`; equity avg `0.7216` n `166`; fx avg `-0.0994` n `6`; index avg `0.2305` n `27`; metal avg `-0.4287` n `20`; unknown avg `0.5335` n `1132`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
