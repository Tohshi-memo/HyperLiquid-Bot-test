# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T20:07:24.981704+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `1.6076` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.6054` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0584` n `12`; crypto_alt avg `-0.551` n `228`; crypto_major avg `-0.5555` n `8`; equity avg `-0.6652` n `74`; fx avg `-0.0087` n `6`; index avg `-0.3308` n `23`; metal avg `-0.3382` n `18`; unknown avg `-0.3257` n `425`
- 1h: commodity avg `-0.0707` n `12`; crypto_alt avg `1.8858` n `228`; crypto_major avg `1.2717` n `8`; equity avg `-0.3337` n `74`; fx avg `-0.0051` n `6`; index avg `-0.2626` n `23`; metal avg `-0.3359` n `18`; unknown avg `1.0255` n `425`
- 4h: commodity avg `-0.3351` n `12`; crypto_alt avg `-0.1357` n `228`; crypto_major avg `-0.4722` n `8`; equity avg `-1.8416` n `74`; fx avg `-0.0458` n `6`; index avg `-1.8773` n `23`; metal avg `-0.8692` n `18`; unknown avg `-0.4267` n `424`
- 24h: commodity avg `-1.6464` n `12`; crypto_alt avg `-8.7114` n `228`; crypto_major avg `-7.1367` n `8`; equity avg `-6.584` n `74`; fx avg `-0.0573` n `6`; index avg `-4.4556` n `23`; metal avg `-4.8863` n `18`; unknown avg `-2.2318` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
