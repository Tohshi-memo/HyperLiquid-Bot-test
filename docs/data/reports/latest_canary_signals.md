# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T11:07:32.449387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6966` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4138` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0823` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0418` n `12`; crypto_alt avg `-0.2641` n `228`; crypto_major avg `-0.4763` n `8`; equity avg `-0.0284` n `86`; fx avg `-0.0121` n `6`; index avg `-0.0055` n `23`; metal avg `0.0344` n `20`; unknown avg `-0.0627` n `765`
- 1h: commodity avg `-0.0701` n `12`; crypto_alt avg `-0.641` n `228`; crypto_major avg `-1.0366` n `8`; equity avg `0.0254` n `86`; fx avg `-0.0276` n `6`; index avg `0.0457` n `23`; metal avg `0.0076` n `20`; unknown avg `-0.0977` n `765`
- 4h: commodity avg `-0.0024` n `12`; crypto_alt avg `-0.8344` n `228`; crypto_major avg `-1.382` n `8`; equity avg `0.07` n `86`; fx avg `-0.0132` n `6`; index avg `0.0318` n `23`; metal avg `0.3146` n `20`; unknown avg `-0.1377` n `757`
- 24h: commodity avg `-0.3393` n `12`; crypto_alt avg `-1.3299` n `228`; crypto_major avg `-1.3621` n `8`; equity avg `0.2852` n `86`; fx avg `-0.0154` n `6`; index avg `0.5379` n `23`; metal avg `-0.9969` n `20`; unknown avg `-0.5937` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
