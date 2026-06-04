# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T15:07:27.929568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2113` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.8698` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1153` n `12`; crypto_alt avg `0.8873` n `228`; crypto_major avg `0.9129` n `8`; equity avg `0.4587` n `74`; fx avg `0.0001` n `6`; index avg `0.284` n `23`; metal avg `0.1322` n `18`; unknown avg `0.1875` n `424`
- 1h: commodity avg `0.0771` n `12`; crypto_alt avg `0.5546` n `228`; crypto_major avg `0.3806` n `8`; equity avg `0.5342` n `74`; fx avg `0.0002` n `6`; index avg `0.6497` n `23`; metal avg `-0.3136` n `18`; unknown avg `0.0884` n `424`
- 4h: commodity avg `-0.2198` n `12`; crypto_alt avg `3.2677` n `228`; crypto_major avg `2.9915` n `8`; equity avg `1.6482` n `73`; fx avg `-0.0016` n `6`; index avg `0.5984` n `23`; metal avg `0.1217` n `18`; unknown avg `1.7768` n `422`
- 24h: commodity avg `-0.4453` n `12`; crypto_alt avg `-5.7447` n `228`; crypto_major avg `-3.6238` n `8`; equity avg `-1.748` n `73`; fx avg `0.0931` n `6`; index avg `-0.6203` n `23`; metal avg `-0.0543` n `18`; unknown avg `-1.109` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1527`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
