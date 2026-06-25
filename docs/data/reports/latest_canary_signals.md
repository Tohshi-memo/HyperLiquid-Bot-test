# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T12:22:27.038263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3131` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0446` n `12`; crypto_alt avg `-0.1773` n `228`; crypto_major avg `-0.1892` n `8`; equity avg `-0.003` n `86`; fx avg `0.0024` n `6`; index avg `-0.0156` n `23`; metal avg `0.0125` n `20`; unknown avg `-0.0961` n `765`
- 1h: commodity avg `0.0753` n `12`; crypto_alt avg `-0.1511` n `228`; crypto_major avg `-0.1419` n `8`; equity avg `-0.0271` n `86`; fx avg `-0.0142` n `6`; index avg `-0.0275` n `23`; metal avg `0.0906` n `20`; unknown avg `-0.0162` n `765`
- 4h: commodity avg `0.0041` n `12`; crypto_alt avg `-1.1699` n `228`; crypto_major avg `-1.318` n `8`; equity avg `-0.1047` n `86`; fx avg `-0.0124` n `6`; index avg `-0.0049` n `23`; metal avg `0.0139` n `20`; unknown avg `-0.1186` n `765`
- 24h: commodity avg `-0.0318` n `12`; crypto_alt avg `-2.1738` n `228`; crypto_major avg `-2.1008` n `8`; equity avg `-0.0822` n `86`; fx avg `-0.0139` n `6`; index avg `0.4155` n `23`; metal avg `-0.5859` n `20`; unknown avg `-0.692` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
