# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T15:22:23.494072+00:00`
- Correlation status: `ready`
- Asset price records: `561`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.67` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.1223` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0895` n `12`; crypto_alt avg `-0.4444` n `228`; crypto_major avg `-0.3234` n `8`; equity avg `-0.1477` n `65`; fx avg `0.0111` n `5`; index avg `-0.0608` n `23`; metal avg `-0.1643` n `18`; unknown avg `-0.1491` n `365`
- 1h: commodity avg `0.9268` n `12`; crypto_alt avg `-0.9192` n `228`; crypto_major avg `-0.5992` n `8`; equity avg `-0.6006` n `65`; fx avg `0.0113` n `5`; index avg `0.0667` n `23`; metal avg `-0.0567` n `18`; unknown avg `-0.3411` n `365`
- 4h: commodity avg `0.3286` n `12`; crypto_alt avg `-1.1307` n `228`; crypto_major avg `-1.366` n `8`; equity avg `-0.5662` n `65`; fx avg `0.0044` n `5`; index avg `-0.2437` n `23`; metal avg `0.304` n `18`; unknown avg `-0.5293` n `365`
- 24h: commodity avg `-0.6706` n `12`; crypto_alt avg `-0.1315` n `228`; crypto_major avg `-2.1963` n `8`; equity avg `0.5553` n `65`; fx avg `0.1077` n `5`; index avg `0.2722` n `23`; metal avg `1.5679` n `18`; unknown avg `-0.2947` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1333`, n `557`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1237`, n `557`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `557`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0995`, n `557`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0978`, n `557`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `553`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0832`, n `553`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.079`, n `553`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.076`, n `557`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0757`, n `553`, weak_sample_signal
