# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T19:22:36.327345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.4959` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `2.2658` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.1548` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.9265` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `0.0252` n `231`; crypto_major avg `0.0349` n `8`; equity avg `-0.0232` n `122`; fx avg `0.0002` n `6`; index avg `0.0048` n `25`; metal avg `0.038` n `20`; unknown avg `-0.016` n `794`
- 1h: commodity avg `0.0781` n `12`; crypto_alt avg `-0.5851` n `231`; crypto_major avg `-0.4558` n `8`; equity avg `-0.2783` n `122`; fx avg `0.0064` n `6`; index avg `-0.0275` n `25`; metal avg `0.0363` n `20`; unknown avg `-0.0204` n `794`
- 4h: commodity avg `0.0007` n `12`; crypto_alt avg `-2.0105` n `231`; crypto_major avg `-2.1541` n `8`; equity avg `0.3418` n `122`; fx avg `-0.0363` n `6`; index avg `0.1117` n `25`; metal avg `-0.2276` n `20`; unknown avg `0.2493` n `793`
- 24h: commodity avg `-0.1318` n `12`; crypto_alt avg `-1.8806` n `231`; crypto_major avg `-0.8593` n `8`; equity avg `-2.6054` n `122`; fx avg `-0.1374` n `6`; index avg `-0.3199` n `25`; metal avg `0.0976` n `20`; unknown avg `2.419` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
