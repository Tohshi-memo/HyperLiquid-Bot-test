# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T23:22:24.262032+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2865` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0646` n `12`; crypto_alt avg `-0.7447` n `228`; crypto_major avg `-0.8991` n `8`; equity avg `-0.1929` n `74`; fx avg `0.0072` n `6`; index avg `-0.0779` n `23`; metal avg `-0.0056` n `18`; unknown avg `-0.1146` n `424`
- 1h: commodity avg `-0.0375` n `12`; crypto_alt avg `-0.0009` n `228`; crypto_major avg `-0.2021` n `8`; equity avg `-0.2791` n `74`; fx avg `0.0072` n `6`; index avg `-0.136` n `23`; metal avg `-0.0901` n `18`; unknown avg `-0.2248` n `424`
- 4h: commodity avg `-0.1855` n `12`; crypto_alt avg `-2.7261` n `228`; crypto_major avg `-1.6782` n `8`; equity avg `-1.1362` n `74`; fx avg `0.0051` n `6`; index avg `-0.3917` n `23`; metal avg `-0.2143` n `18`; unknown avg `-1.1079` n `424`
- 24h: commodity avg `-0.5909` n `12`; crypto_alt avg `-6.7881` n `228`; crypto_major avg `-4.472` n `8`; equity avg `-0.3088` n `73`; fx avg `0.055` n `6`; index avg `0.1972` n `23`; metal avg `0.6606` n `18`; unknown avg `-1.5259` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
