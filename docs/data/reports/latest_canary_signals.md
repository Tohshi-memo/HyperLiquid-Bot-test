# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T22:52:25.478222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5614` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3192` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0001` n `12`; crypto_alt avg `0.2925` n `228`; crypto_major avg `0.3209` n `8`; equity avg `0.0462` n `74`; fx avg `-0.0077` n `6`; index avg `-0.085` n `23`; metal avg `-0.0509` n `18`; unknown avg `0.4022` n `424`
- 1h: commodity avg `-0.015` n `12`; crypto_alt avg `-0.2158` n `228`; crypto_major avg `-0.007` n `8`; equity avg `-0.2693` n `74`; fx avg `-0.0116` n `6`; index avg `-0.3268` n `23`; metal avg `0.0153` n `18`; unknown avg `-0.6131` n `424`
- 4h: commodity avg `-0.1146` n `12`; crypto_alt avg `-2.7983` n `228`; crypto_major avg `-1.7379` n `8`; equity avg `-1.1285` n `74`; fx avg `-0.0272` n `6`; index avg `-0.4187` n `23`; metal avg `-0.1765` n `18`; unknown avg `-0.8801` n `424`
- 24h: commodity avg `-0.5757` n `12`; crypto_alt avg `-7.3902` n `228`; crypto_major avg `-4.8546` n `8`; equity avg `-0.3625` n `73`; fx avg `0.0695` n `6`; index avg `0.1732` n `23`; metal avg `0.8952` n `18`; unknown avg `-1.5458` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
