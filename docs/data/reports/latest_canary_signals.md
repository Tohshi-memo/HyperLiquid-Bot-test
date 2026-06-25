# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T15:07:32.265055+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.1627` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.1206` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.5295` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2832` n `12`; crypto_alt avg `-0.4644` n `228`; crypto_major avg `-0.6606` n `8`; equity avg `-0.3326` n `86`; fx avg `0.0354` n `6`; index avg `-0.0528` n `23`; metal avg `-0.008` n `20`; unknown avg `-0.3448` n `765`
- 1h: commodity avg `0.107` n `12`; crypto_alt avg `0.6477` n `228`; crypto_major avg `0.1098` n `8`; equity avg `0.154` n `86`; fx avg `0.0308` n `6`; index avg `0.0234` n `23`; metal avg `0.1341` n `20`; unknown avg `0.5988` n `765`
- 4h: commodity avg `0.3589` n `12`; crypto_alt avg `-2.1634` n `228`; crypto_major avg `-2.8038` n `8`; equity avg `-2.4869` n `86`; fx avg `0.0536` n `6`; index avg `-0.2743` n `23`; metal avg `0.3168` n `20`; unknown avg `1.0562` n `765`
- 24h: commodity avg `0.4183` n `12`; crypto_alt avg `-2.4119` n `228`; crypto_major avg `-2.8005` n `8`; equity avg `-1.1149` n `86`; fx avg `0.0737` n `6`; index avg `0.2665` n `23`; metal avg `0.1178` n `20`; unknown avg `0.292` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
