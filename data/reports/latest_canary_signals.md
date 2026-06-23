# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T10:00:56.989092+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.0339` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.0072` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.8692` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0184` n `12`; crypto_alt avg `0.0343` n `228`; crypto_major avg `0.0386` n `8`; equity avg `0.0988` n `86`; fx avg `0.0003` n `6`; index avg `0.0092` n `23`; metal avg `0.0967` n `20`; unknown avg `0.01` n `764`
- 1h: commodity avg `-0.025` n `12`; crypto_alt avg `0.1899` n `228`; crypto_major avg `0.0698` n `8`; equity avg `0.2767` n `86`; fx avg `-0.0243` n `6`; index avg `0.0615` n `23`; metal avg `0.2617` n `20`; unknown avg `-0.128` n `764`
- 4h: commodity avg `0.0196` n `12`; crypto_alt avg `-1.8474` n `228`; crypto_major avg `-1.9301` n `8`; equity avg `0.0771` n `86`; fx avg `-0.0792` n `6`; index avg `-0.0609` n `23`; metal avg `0.1038` n `20`; unknown avg `-0.4232` n `620`
- 24h: commodity avg `-0.6628` n `12`; crypto_alt avg `-3.88` n `228`; crypto_major avg `-4.1809` n `8`; equity avg `-4.2413` n `85`; fx avg `-0.1275` n `6`; index avg `-0.8233` n `23`; metal avg `-1.3405` n `18`; unknown avg `0.6284` n `583`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
