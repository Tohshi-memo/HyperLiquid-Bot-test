# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T17:37:43.875918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3134` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.1211` n `12`; crypto_alt avg `-0.4157` n `228`; crypto_major avg `-0.413` n `8`; equity avg `0.0107` n `74`; fx avg `-0.0196` n `6`; index avg `-0.0051` n `23`; metal avg `-0.1179` n `18`; unknown avg `0.0108` n `549`
- 1h: commodity avg `0.1797` n `12`; crypto_alt avg `-1.0766` n `228`; crypto_major avg `-1.0774` n `8`; equity avg `-0.7148` n `74`; fx avg `-0.0147` n `6`; index avg `-0.4151` n `23`; metal avg `-0.6479` n `18`; unknown avg `0.1087` n `548`
- 4h: commodity avg `0.8328` n `12`; crypto_alt avg `-1.4753` n `228`; crypto_major avg `-1.4806` n `8`; equity avg `-0.9771` n `74`; fx avg `-0.0654` n `6`; index avg `-0.6816` n `23`; metal avg `-0.8515` n `18`; unknown avg `2.5175` n `547`
- 24h: commodity avg `1.8087` n `12`; crypto_alt avg `-1.1434` n `228`; crypto_major avg `-1.8371` n `8`; equity avg `-0.3051` n `74`; fx avg `-0.0651` n `6`; index avg `0.0025` n `23`; metal avg `-1.5412` n `18`; unknown avg `-0.1548` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
