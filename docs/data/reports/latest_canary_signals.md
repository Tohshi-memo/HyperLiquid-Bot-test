# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T16:52:24.955742+00:00`
- Correlation status: `ready`
- Asset price records: `471`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `6.64` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.7221` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.684` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5701` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.5143` n `12`; crypto_alt avg `0.4155` n `228`; crypto_major avg `0.2599` n `8`; equity avg `-0.0458` n `65`; fx avg `0.0211` n `4`; index avg `-0.0056` n `23`; metal avg `-0.1222` n `18`; unknown avg `0.0574` n `356`
- 1h: commodity avg `0.2186` n `12`; crypto_alt avg `0.2447` n `228`; crypto_major avg `0.0599` n `8`; equity avg `0.0401` n `65`; fx avg `0.045` n `4`; index avg `0.0202` n `23`; metal avg `-0.161` n `18`; unknown avg `0.0036` n `356`
- 4h: commodity avg `0.0103` n `7`; crypto_alt avg `-0.7252` n `223`; crypto_major avg `-1.5165` n `7`; equity avg `0.0536` n `47`; fx avg `0.0405` n `4`; index avg `0.1675` n `6`; metal avg `0.2056` n `7`; unknown avg `7.6445` n `313`
- 24h: commodity avg `-2.2173` n `7`; crypto_alt avg `3.4899` n `223`; crypto_major avg `1.4917` n `7`; equity avg `2.457` n `47`; fx avg `-0.4073` n `4`; index avg `1.981` n `6`; metal avg `3.0362` n `7`; unknown avg `16.4044` n `311`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1986`, n `467`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1538`, n `463`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.137`, n `463`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1349`, n `467`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `467`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1212`, n `467`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1122`, n `463`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1111`, n `467`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1069`, n `467`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0971`, n `463`, weak_sample_signal
