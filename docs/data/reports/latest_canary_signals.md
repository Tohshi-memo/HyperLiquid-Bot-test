# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T09:22:26.051737+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `-11.8872` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `-10.5559` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0563` n `12`; crypto_alt avg `0.0489` n `228`; crypto_major avg `-0.0265` n `8`; equity avg `11.606` n `74`; fx avg `-0.0065` n `6`; index avg `-0.1106` n `23`; metal avg `-0.0268` n `18`; unknown avg `-0.2044` n `425`
- 1h: commodity avg `0.1692` n `12`; crypto_alt avg `0.3422` n `228`; crypto_major avg `-0.003` n `8`; equity avg `11.8842` n `74`; fx avg `-0.0063` n `6`; index avg `0.4793` n `23`; metal avg `0.0775` n `18`; unknown avg `-0.173` n `425`
- 4h: commodity avg `0.1397` n `12`; crypto_alt avg `2.2785` n `228`; crypto_major avg `1.4405` n `8`; equity avg `11.9964` n `74`; fx avg `-0.0195` n `6`; index avg `0.6672` n `23`; metal avg `0.4209` n `18`; unknown avg `0.3472` n `415`
- 24h: commodity avg `-1.0141` n `12`; crypto_alt avg `-3.1242` n `228`; crypto_major avg `-3.1102` n `8`; equity avg `3.9637` n `74`; fx avg `-0.2672` n `6`; index avg `-3.8293` n `23`; metal avg `-4.2684` n `18`; unknown avg `0.5499` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
