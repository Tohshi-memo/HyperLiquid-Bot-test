# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T04:05:03.089504+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.9105` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `-0.0766` n `231`; crypto_major avg `-0.0959` n `8`; equity avg `0.1765` n `122`; fx avg `-0.0072` n `6`; index avg `0.0552` n `25`; metal avg `-0.0024` n `20`; unknown avg `0.5743` n `794`
- 1h: commodity avg `0.0256` n `12`; crypto_alt avg `-0.3576` n `231`; crypto_major avg `-0.5208` n `8`; equity avg `0.3347` n `122`; fx avg `0.0029` n `6`; index avg `0.0742` n `25`; metal avg `0.0032` n `20`; unknown avg `0.5713` n `794`
- 4h: commodity avg `0.053` n `12`; crypto_alt avg `1.0481` n `231`; crypto_major avg `1.4795` n `8`; equity avg `0.9899` n `122`; fx avg `0.0442` n `6`; index avg `0.1856` n `25`; metal avg `-0.431` n `20`; unknown avg `0.3581` n `794`
- 24h: commodity avg `0.05` n `12`; crypto_alt avg `1.8616` n `231`; crypto_major avg `2.6666` n `8`; equity avg `-0.4378` n `122`; fx avg `0.022` n `6`; index avg `-0.0666` n `25`; metal avg `-0.1381` n `20`; unknown avg `0.6246` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
