# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T23:37:22.331826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3734` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.1008` n `12`; crypto_alt avg `0.0908` n `228`; crypto_major avg `0.0824` n `8`; equity avg `0.0384` n `67`; fx avg `-0.004` n `6`; index avg `0.0328` n `23`; metal avg `0.0436` n `18`; unknown avg `-0.0696` n `396`
- 1h: commodity avg `0.1453` n `12`; crypto_alt avg `0.323` n `228`; crypto_major avg `0.4934` n `8`; equity avg `0.1765` n `67`; fx avg `0.0032` n `6`; index avg `0.2057` n `23`; metal avg `0.1886` n `18`; unknown avg `-0.2396` n `396`
- 4h: commodity avg `-1.5251` n `12`; crypto_alt avg `0.6634` n `228`; crypto_major avg `0.8483` n `8`; equity avg `0.8303` n `67`; fx avg `0.0807` n `6`; index avg `0.3704` n `23`; metal avg `0.5776` n `18`; unknown avg `0.116` n `396`
- 24h: commodity avg `-2.942` n `12`; crypto_alt avg `2.0142` n `228`; crypto_major avg `1.6642` n `8`; equity avg `1.6884` n `67`; fx avg `0.0545` n `6`; index avg `0.8408` n `23`; metal avg `0.7946` n `18`; unknown avg `0.0553` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
