# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T19:22:26.603346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `0.3389` n `228`; crypto_major avg `0.2331` n `8`; equity avg `-0.0207` n `74`; fx avg `-0.0151` n `6`; index avg `-0.0609` n `23`; metal avg `-0.0127` n `18`; unknown avg `0.3608` n `424`
- 1h: commodity avg `0.4789` n `12`; crypto_alt avg `0.7759` n `228`; crypto_major avg `0.5998` n `8`; equity avg `-0.136` n `74`; fx avg `-0.0213` n `6`; index avg `-0.0401` n `23`; metal avg `-0.0531` n `18`; unknown avg `0.6438` n `424`
- 4h: commodity avg `0.1947` n `12`; crypto_alt avg `0.1246` n `228`; crypto_major avg `0.1596` n `8`; equity avg `-0.177` n `74`; fx avg `-0.0416` n `6`; index avg `0.2619` n `23`; metal avg `0.1849` n `18`; unknown avg `2.3102` n `424`
- 24h: commodity avg `-0.5454` n `12`; crypto_alt avg `-4.7004` n `228`; crypto_major avg `-3.2259` n `8`; equity avg `-1.0174` n `73`; fx avg `0.0273` n `6`; index avg `0.0205` n `23`; metal avg `0.7798` n `18`; unknown avg `1.275` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
