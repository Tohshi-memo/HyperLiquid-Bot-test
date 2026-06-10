# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T23:07:27.719224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0744` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.1602` n `12`; crypto_alt avg `-0.1547` n `228`; crypto_major avg `-0.1882` n `8`; equity avg `-0.2509` n `74`; fx avg `-0.0204` n `6`; index avg `-0.0815` n `23`; metal avg `-0.3685` n `18`; unknown avg `-0.1414` n `550`
- 1h: commodity avg `0.3221` n `12`; crypto_alt avg `0.5865` n `228`; crypto_major avg `0.1906` n `8`; equity avg `-0.3447` n `74`; fx avg `-0.0159` n `6`; index avg `-0.0484` n `23`; metal avg `-0.164` n `18`; unknown avg `0.0024` n `550`
- 4h: commodity avg `0.8495` n `12`; crypto_alt avg `-1.8008` n `228`; crypto_major avg `-1.2249` n `8`; equity avg `-1.7501` n `74`; fx avg `-0.095` n `6`; index avg `-0.6259` n `23`; metal avg `-1.338` n `18`; unknown avg `-0.249` n `550`
- 24h: commodity avg `1.7733` n `12`; crypto_alt avg `-2.5456` n `228`; crypto_major avg `-2.6777` n `8`; equity avg `-2.6406` n `74`; fx avg `-0.1168` n `6`; index avg `-1.8341` n `23`; metal avg `-2.9401` n `18`; unknown avg `-0.4758` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0652`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
