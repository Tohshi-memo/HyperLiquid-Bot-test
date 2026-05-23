# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T22:22:16.537723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8719` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0416` n `12`; crypto_alt avg `-0.204` n `228`; crypto_major avg `-0.2278` n `8`; equity avg `-0.0253` n `67`; fx avg `0.0258` n `6`; index avg `-0.0709` n `23`; metal avg `-0.0139` n `18`; unknown avg `0.178` n `396`
- 1h: commodity avg `0.3609` n `12`; crypto_alt avg `-0.5654` n `228`; crypto_major avg `-0.7505` n `8`; equity avg `-0.0802` n `67`; fx avg `0.0335` n `6`; index avg `-0.1768` n `23`; metal avg `-0.1723` n `18`; unknown avg `0.0435` n `396`
- 4h: commodity avg `-2.0858` n `12`; crypto_alt avg `1.0565` n `228`; crypto_major avg `0.7861` n `8`; equity avg `1.0608` n `67`; fx avg `0.0728` n `6`; index avg `0.5366` n `23`; metal avg `0.416` n `18`; unknown avg `0.3709` n `396`
- 24h: commodity avg `-2.6183` n `12`; crypto_alt avg `1.7829` n `228`; crypto_major avg `1.267` n `8`; equity avg `1.3938` n `67`; fx avg `0.0559` n `6`; index avg `0.6898` n `23`; metal avg `0.5378` n `18`; unknown avg `-0.3148` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
