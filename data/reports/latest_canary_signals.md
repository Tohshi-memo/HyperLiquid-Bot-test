# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T15:37:31.828487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0192` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9913` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0236` n `12`; crypto_alt avg `0.1847` n `228`; crypto_major avg `0.1571` n `8`; equity avg `-0.0084` n `74`; fx avg `0.0013` n `6`; index avg `-0.0207` n `23`; metal avg `0.076` n `18`; unknown avg `-0.0367` n `424`
- 1h: commodity avg `0.1722` n `12`; crypto_alt avg `1.0242` n `228`; crypto_major avg `0.2836` n `8`; equity avg `0.5202` n `74`; fx avg `-0.02` n `6`; index avg `0.3248` n `23`; metal avg `0.0165` n `18`; unknown avg `-0.2164` n `424`
- 4h: commodity avg `0.02` n `12`; crypto_alt avg `3.2358` n `228`; crypto_major avg `2.0392` n `8`; equity avg `1.8469` n `73`; fx avg `-0.0229` n `6`; index avg `0.7883` n `23`; metal avg `0.0479` n `18`; unknown avg `1.4136` n `422`
- 24h: commodity avg `-0.7132` n `12`; crypto_alt avg `-5.4399` n `228`; crypto_major avg `-4.0948` n `8`; equity avg `-1.2952` n `73`; fx avg `0.0612` n `6`; index avg `-0.3322` n `23`; metal avg `0.3349` n `18`; unknown avg `-1.1807` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
