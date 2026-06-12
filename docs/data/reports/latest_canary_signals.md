# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T04:52:29.631135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0164` n `12`; crypto_alt avg `0.054` n `228`; crypto_major avg `0.0291` n `8`; equity avg `0.0388` n `74`; fx avg `-0.0046` n `6`; index avg `0.0295` n `23`; metal avg `-0.0401` n `18`; unknown avg `-0.0639` n `557`
- 1h: commodity avg `-0.2197` n `12`; crypto_alt avg `0.2339` n `228`; crypto_major avg `0.2267` n `8`; equity avg `0.0772` n `74`; fx avg `0.007` n `6`; index avg `0.1297` n `23`; metal avg `-0.1454` n `18`; unknown avg `1.2025` n `557`
- 4h: commodity avg `-0.1167` n `12`; crypto_alt avg `0.0766` n `228`; crypto_major avg `0.106` n `8`; equity avg `-0.3027` n `74`; fx avg `0.053` n `6`; index avg `-0.0056` n `23`; metal avg `-0.0272` n `18`; unknown avg `2.1573` n `556`
- 24h: commodity avg `-2.3639` n `12`; crypto_alt avg `1.6181` n `228`; crypto_major avg `2.3913` n `8`; equity avg `3.6651` n `74`; fx avg `0.0126` n `6`; index avg `1.9665` n `23`; metal avg `2.8945` n `18`; unknown avg `1.7694` n `530`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
