# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T17:33:39.336454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.314` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.121` n `12`; crypto_alt avg `-0.4543` n `228`; crypto_major avg `-0.4137` n `8`; equity avg `0.0164` n `74`; fx avg `-0.0198` n `6`; index avg `-0.0168` n `23`; metal avg `-0.0909` n `18`; unknown avg `0.0271` n `549`
- 1h: commodity avg `0.1798` n `12`; crypto_alt avg `-1.115` n `228`; crypto_major avg `-1.0781` n `8`; equity avg `-0.7086` n `74`; fx avg `-0.0149` n `6`; index avg `-0.4266` n `23`; metal avg `-0.6212` n `18`; unknown avg `0.1212` n `548`
- 4h: commodity avg `0.8334` n `12`; crypto_alt avg `-1.5133` n `228`; crypto_major avg `-1.4806` n `8`; equity avg `-0.9709` n `74`; fx avg `-0.0655` n `6`; index avg `-0.693` n `23`; metal avg `-0.8248` n `18`; unknown avg `2.5326` n `547`
- 24h: commodity avg `1.809` n `12`; crypto_alt avg `-1.1799` n `228`; crypto_major avg `-1.8363` n `8`; equity avg `-0.2982` n `74`; fx avg `-0.0653` n `6`; index avg `-0.0092` n `23`; metal avg `-1.5145` n `18`; unknown avg `-0.1414` n `537`

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
