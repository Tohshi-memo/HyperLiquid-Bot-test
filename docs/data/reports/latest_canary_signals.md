# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T18:07:19.113808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.44` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.3381` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.2323` n `12`; crypto_alt avg `-0.2548` n `228`; crypto_major avg `-0.381` n `8`; equity avg `-0.1063` n `67`; fx avg `-0.0094` n `6`; index avg `-0.0479` n `23`; metal avg `-0.2684` n `18`; unknown avg `-0.8154` n `386`
- 1h: commodity avg `-1.2478` n `12`; crypto_alt avg `1.186` n `228`; crypto_major avg `0.6574` n `8`; equity avg `0.8696` n `67`; fx avg `-0.0013` n `6`; index avg `0.592` n `23`; metal avg `0.6322` n `18`; unknown avg `0.6884` n `385`
- 4h: commodity avg `-1.4308` n `12`; crypto_alt avg `1.7243` n `228`; crypto_major avg `0.9073` n `8`; equity avg `1.0526` n `67`; fx avg `-0.0035` n `6`; index avg `0.4093` n `23`; metal avg `1.3567` n `18`; unknown avg `1.3426` n `385`
- 24h: commodity avg `-0.6088` n `12`; crypto_alt avg `2.003` n `228`; crypto_major avg `2.2137` n `8`; equity avg `1.7174` n `66`; fx avg `0.0099` n `6`; index avg `0.8141` n `23`; metal avg `0.1924` n `18`; unknown avg `5.8932` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
