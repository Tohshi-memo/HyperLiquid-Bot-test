# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T22:37:39.113747+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1487` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.1453` n `12`; crypto_alt avg `-0.6244` n `228`; crypto_major avg `-0.3941` n `8`; equity avg `-0.0759` n `67`; fx avg `-0.0005` n `6`; index avg `-0.129` n `23`; metal avg `0.017` n `18`; unknown avg `0.0111` n `396`
- 1h: commodity avg `-0.1953` n `12`; crypto_alt avg `-0.992` n `228`; crypto_major avg `-0.7619` n `8`; equity avg `-0.0844` n `67`; fx avg `0.0496` n `6`; index avg `-0.1417` n `23`; metal avg `-0.0094` n `18`; unknown avg `-0.4148` n `396`
- 4h: commodity avg `-1.8553` n `12`; crypto_alt avg `0.25` n `228`; crypto_major avg `0.2934` n `8`; equity avg `0.5958` n `67`; fx avg `0.0701` n `6`; index avg `0.0452` n `23`; metal avg `0.4033` n `18`; unknown avg `0.2394` n `396`
- 24h: commodity avg `-2.7415` n `12`; crypto_alt avg `1.3996` n `228`; crypto_major avg `1.0207` n `8`; equity avg `1.3843` n `67`; fx avg `0.054` n `6`; index avg `0.5576` n `23`; metal avg `0.5623` n `18`; unknown avg `-0.1455` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
