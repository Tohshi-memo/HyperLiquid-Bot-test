# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T11:22:33.979305+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.9755` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6077` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `-0.1852` n `228`; crypto_major avg `-0.2348` n `8`; equity avg `-0.0962` n `86`; fx avg `0.0109` n `6`; index avg `0.0012` n `23`; metal avg `-0.0184` n `20`; unknown avg `-0.0841` n `765`
- 1h: commodity avg `0.0832` n `12`; crypto_alt avg `-0.3842` n `228`; crypto_major avg `-0.3812` n `8`; equity avg `0.0677` n `86`; fx avg `0.0029` n `6`; index avg `0.0218` n `23`; metal avg `0.1587` n `20`; unknown avg `-0.0883` n `765`
- 4h: commodity avg `-0.0901` n `12`; crypto_alt avg `-1.3642` n `228`; crypto_major avg `-1.6649` n `8`; equity avg `-0.4878` n `86`; fx avg `0.0343` n `6`; index avg `-0.0572` n `23`; metal avg `0.3106` n `20`; unknown avg `-0.1577` n `765`
- 24h: commodity avg `0.0976` n `12`; crypto_alt avg `-1.883` n `228`; crypto_major avg `-1.8898` n `8`; equity avg `-4.0787` n `86`; fx avg `0.0703` n `6`; index avg `-0.6134` n `23`; metal avg `0.757` n `20`; unknown avg `0.7052` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.269`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
