# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T16:37:38.310221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0566` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.5454` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.281` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.8409` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0339` n `13`; crypto_alt avg `-0.8566` n `239`; crypto_major avg `-0.721` n `8`; equity avg `-0.2499` n `160`; fx avg `-0.0134` n `6`; index avg `-0.0183` n `27`; metal avg `-0.0408` n `20`; unknown avg `0.9248` n `1262`
- 1h: commodity avg `0.481` n `13`; crypto_alt avg `-1.0485` n `239`; crypto_major avg `-1.0324` n `8`; equity avg `-0.7219` n `160`; fx avg `-0.0486` n `6`; index avg `-0.0724` n `27`; metal avg `-0.2102` n `20`; unknown avg `19.555` n `1250`
- 4h: commodity avg `0.4223` n `13`; crypto_alt avg `-1.5466` n `239`; crypto_major avg `-2.6343` n `8`; equity avg `-0.7934` n `160`; fx avg `-0.1145` n `6`; index avg `-0.0889` n `27`; metal avg `-0.3533` n `20`; unknown avg `19.0378` n `1250`
- 24h: commodity avg `-0.1889` n `13`; crypto_alt avg `-2.4446` n `239`; crypto_major avg `-4.0478` n `8`; equity avg `-1.215` n `160`; fx avg `-0.1361` n `6`; index avg `-0.0799` n `27`; metal avg `-0.5459` n `20`; unknown avg `1.7921` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2361`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
