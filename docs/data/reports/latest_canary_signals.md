# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T23:52:15.698013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5818` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.1104` n `12`; crypto_alt avg `-0.0119` n `228`; crypto_major avg `-0.0103` n `8`; equity avg `-0.0011` n `67`; fx avg `-0.0002` n `6`; index avg `0.0386` n `23`; metal avg `0.0444` n `18`; unknown avg `0.315` n `396`
- 1h: commodity avg `0.0136` n `12`; crypto_alt avg `0.0826` n `228`; crypto_major avg `0.2006` n `8`; equity avg `0.0876` n `67`; fx avg `0.0037` n `6`; index avg `0.2558` n `23`; metal avg `0.1592` n `18`; unknown avg `0.0982` n `396`
- 4h: commodity avg `-1.7674` n `12`; crypto_alt avg `0.6962` n `228`; crypto_major avg `0.8144` n `8`; equity avg `0.7627` n `67`; fx avg `0.1087` n `6`; index avg `0.3194` n `23`; metal avg `0.6092` n `18`; unknown avg `0.4447` n `396`
- 24h: commodity avg `-3.0495` n `12`; crypto_alt avg `2.7477` n `228`; crypto_major avg `1.8965` n `8`; equity avg `1.7644` n `67`; fx avg `0.0572` n `6`; index avg `0.8499` n `23`; metal avg `0.8962` n `18`; unknown avg `0.8914` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
