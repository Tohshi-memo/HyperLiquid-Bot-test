# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T16:29:26.873296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1795` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.016` n `12`; crypto_alt avg `-0.0418` n `228`; crypto_major avg `-0.1842` n `8`; equity avg `-0.053` n `67`; fx avg `0.0044` n `6`; index avg `-0.0279` n `23`; metal avg `-0.0283` n `18`; unknown avg `-0.1589` n `396`
- 1h: commodity avg `-0.207` n `12`; crypto_alt avg `0.0431` n `228`; crypto_major avg `-0.2053` n `8`; equity avg `-0.0388` n `67`; fx avg `0.0125` n `6`; index avg `-0.0936` n `23`; metal avg `-0.0274` n `18`; unknown avg `0.1987` n `396`
- 4h: commodity avg `-0.6484` n `12`; crypto_alt avg `2.3853` n `228`; crypto_major avg `1.5311` n `8`; equity avg `0.7761` n `67`; fx avg `0.0056` n `6`; index avg `0.3003` n `23`; metal avg `0.186` n `18`; unknown avg `0.9952` n `396`
- 24h: commodity avg `0.0007` n `12`; crypto_alt avg `-2.9712` n `228`; crypto_major avg `-2.0316` n `8`; equity avg `-0.9397` n `67`; fx avg `0.0333` n `6`; index avg `-0.2086` n `23`; metal avg `-0.1821` n `18`; unknown avg `-1.6631` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0884`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.074`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0704`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0674`, n `669`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0649`, n `669`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0626`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0626`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0582`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0555`, n `669`, weak_sample_signal
