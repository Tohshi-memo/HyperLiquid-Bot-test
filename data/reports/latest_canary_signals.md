# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T15:37:35.338614+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.742` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `1.6226` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0481` n `13`; crypto_alt avg `0.4192` n `236`; crypto_major avg `0.308` n `8`; equity avg `-0.1689` n `151`; fx avg `0.0092` n `6`; index avg `-0.0363` n `26`; metal avg `-0.0517` n `20`; unknown avg `-0.2223` n `1136`
- 1h: commodity avg `0.0971` n `13`; crypto_alt avg `2.2857` n `236`; crypto_major avg `1.6304` n `8`; equity avg `1.5701` n `151`; fx avg `-0.0223` n `6`; index avg `0.1579` n `26`; metal avg `0.0078` n `20`; unknown avg `0.715` n `1130`
- 4h: commodity avg `0.2283` n `13`; crypto_alt avg `2.9654` n `236`; crypto_major avg `1.7169` n `8`; equity avg `1.1464` n `151`; fx avg `-0.0038` n `6`; index avg `0.1886` n `26`; metal avg `-0.0251` n `20`; unknown avg `3.9565` n `1082`
- 24h: commodity avg `0.1406` n `13`; crypto_alt avg `0.2647` n `236`; crypto_major avg `0.0743` n `8`; equity avg `-2.2127` n `151`; fx avg `0.2108` n `6`; index avg `-0.3825` n `26`; metal avg `0.3157` n `20`; unknown avg `0.4957` n `938`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1116`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0965`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0849`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0792`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0719`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0668`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0633`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
