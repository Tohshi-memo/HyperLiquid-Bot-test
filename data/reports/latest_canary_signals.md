# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T15:52:19.629207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.0698` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.1266` n `12`; crypto_alt avg `0.0954` n `228`; crypto_major avg `0.0854` n `8`; equity avg `0.0489` n `66`; fx avg `-0.0008` n `6`; index avg `0.1111` n `23`; metal avg `0.1085` n `18`; unknown avg `-0.2112` n `384`
- 1h: commodity avg `-0.6782` n `12`; crypto_alt avg `0.4726` n `228`; crypto_major avg `0.153` n `8`; equity avg `0.4581` n `66`; fx avg `0.0243` n `6`; index avg `0.168` n `23`; metal avg `0.1973` n `18`; unknown avg `-0.0478` n `384`
- 4h: commodity avg `-1.9158` n `12`; crypto_alt avg `1.7437` n `228`; crypto_major avg `1.154` n `8`; equity avg `0.8992` n `66`; fx avg `-0.0199` n `6`; index avg `0.8115` n `23`; metal avg `0.7` n `18`; unknown avg `0.5555` n `384`
- 24h: commodity avg `-2.1244` n `12`; crypto_alt avg `2.8407` n `228`; crypto_major avg `1.898` n `8`; equity avg `2.3313` n `66`; fx avg `-0.074` n `6`; index avg `1.4203` n `23`; metal avg `1.4056` n `18`; unknown avg `1.0224` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0459`, n `668`, weak_sample_signal
