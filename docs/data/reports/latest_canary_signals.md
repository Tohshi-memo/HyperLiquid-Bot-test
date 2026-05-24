# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T00:07:15.731217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.448` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.055` n `12`; crypto_alt avg `-0.045` n `228`; crypto_major avg `-0.0175` n `8`; equity avg `0.0053` n `67`; fx avg `-0.0108` n `6`; index avg `0.0364` n `23`; metal avg `0.0297` n `18`; unknown avg `0.1459` n `396`
- 1h: commodity avg `-0.1437` n `12`; crypto_alt avg `-0.0255` n `228`; crypto_major avg `0.0765` n `8`; equity avg `0.0747` n `67`; fx avg `-0.0076` n `6`; index avg `0.1709` n `23`; metal avg `0.1369` n `18`; unknown avg `0.3281` n `396`
- 4h: commodity avg `-1.5877` n `12`; crypto_alt avg `0.7185` n `228`; crypto_major avg `0.8603` n `8`; equity avg `0.7912` n `67`; fx avg `0.0744` n `6`; index avg `0.3137` n `23`; metal avg `0.6476` n `18`; unknown avg `0.4556` n `396`
- 24h: commodity avg `-2.905` n `12`; crypto_alt avg `2.6725` n `228`; crypto_major avg `2.0255` n `8`; equity avg `1.8784` n `67`; fx avg `0.048` n `6`; index avg `0.907` n `23`; metal avg `0.9382` n `18`; unknown avg `0.8961` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
