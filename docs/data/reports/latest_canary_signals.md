# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T21:52:17.762665+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.837` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0532` n `12`; crypto_alt avg `-0.3795` n `228`; crypto_major avg `-0.4135` n `8`; equity avg `-0.0817` n `67`; fx avg `0.0093` n `6`; index avg `0.0102` n `23`; metal avg `-0.0454` n `18`; unknown avg `-0.5044` n `396`
- 1h: commodity avg `-0.6257` n `12`; crypto_alt avg `-0.4051` n `228`; crypto_major avg `-0.655` n `8`; equity avg `0.1928` n `67`; fx avg `0.004` n `6`; index avg `0.0555` n `23`; metal avg `-0.1026` n `18`; unknown avg `0.2673` n `396`
- 4h: commodity avg `-2.3462` n `12`; crypto_alt avg `2.0127` n `228`; crypto_major avg `1.4908` n `8`; equity avg `1.1991` n `67`; fx avg `0.0295` n `6`; index avg `0.6558` n `23`; metal avg `0.4589` n `18`; unknown avg `3.0608` n `396`
- 24h: commodity avg `-2.4204` n `12`; crypto_alt avg `1.3724` n `228`; crypto_major avg `0.8747` n `8`; equity avg `1.2524` n `67`; fx avg `0.0179` n `6`; index avg `0.709` n `23`; metal avg `0.5267` n `18`; unknown avg `-0.4671` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
