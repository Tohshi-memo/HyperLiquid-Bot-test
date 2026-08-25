# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T10:37:33.686836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6986` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.3382` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `-0.0999` n `231`; crypto_major avg `-0.0162` n `8`; equity avg `-0.0267` n `122`; fx avg `-0.0121` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0052` n `20`; unknown avg `0.0311` n `795`
- 1h: commodity avg `0.0361` n `12`; crypto_alt avg `-0.662` n `231`; crypto_major avg `-0.7472` n `8`; equity avg `0.0801` n `122`; fx avg `-0.0215` n `6`; index avg `0.0076` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.0472` n `794`
- 4h: commodity avg `-0.3811` n `12`; crypto_alt avg `-1.2812` n `231`; crypto_major avg `-1.2583` n `8`; equity avg `0.4403` n `122`; fx avg `-0.0159` n `6`; index avg `0.0799` n `25`; metal avg `-0.1605` n `20`; unknown avg `-0.1957` n `794`
- 24h: commodity avg `-0.6284` n `12`; crypto_alt avg `-0.0856` n `227`; crypto_major avg `0.8469` n `8`; equity avg `0.5443` n `106`; fx avg `0.029` n `6`; index avg `0.1166` n `25`; metal avg `-0.2544` n `20`; unknown avg `-0.1152` n `769`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
