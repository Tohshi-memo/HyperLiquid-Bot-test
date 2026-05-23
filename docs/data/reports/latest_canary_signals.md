# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T20:22:18.720408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5419` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.555` n `12`; crypto_alt avg `0.0846` n `228`; crypto_major avg `0.2457` n `8`; equity avg `0.0368` n `67`; fx avg `0.0` n `6`; index avg `-0.0123` n `23`; metal avg `0.0358` n `18`; unknown avg `-0.0477` n `396`
- 1h: commodity avg `-0.5401` n `12`; crypto_alt avg `-0.0356` n `228`; crypto_major avg `0.1728` n `8`; equity avg `0.0568` n `67`; fx avg `-0.0084` n `6`; index avg `0.107` n `23`; metal avg `0.0245` n `18`; unknown avg `0.0009` n `396`
- 4h: commodity avg `-1.3597` n `12`; crypto_alt avg `1.3443` n `228`; crypto_major avg `1.1822` n `8`; equity avg `0.6547` n `67`; fx avg `-0.013` n `6`; index avg `0.4513` n `23`; metal avg `0.2032` n `18`; unknown avg `1.6461` n `396`
- 24h: commodity avg `-1.1331` n `12`; crypto_alt avg `1.0158` n `228`; crypto_major avg `0.9738` n `8`; equity avg `0.6228` n `67`; fx avg `-0.0396` n `6`; index avg `0.3618` n `23`; metal avg `0.1996` n `18`; unknown avg `-0.4755` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
