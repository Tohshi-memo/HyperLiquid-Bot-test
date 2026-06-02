# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T23:07:20.845781+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.52` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-2.0523` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-2.0181` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.8049` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1733` n `12`; crypto_alt avg `0.3919` n `228`; crypto_major avg `0.6316` n `8`; equity avg `-0.0218` n `69`; fx avg `0.0046` n `6`; index avg `-0.028` n `23`; metal avg `-0.1273` n `18`; unknown avg `-0.0638` n `422`
- 1h: commodity avg `0.2818` n `12`; crypto_alt avg `-1.0191` n `228`; crypto_major avg `-0.8426` n `8`; equity avg `-0.3216` n `69`; fx avg `-0.0037` n `6`; index avg `-0.0139` n `23`; metal avg `-0.2603` n `18`; unknown avg `-0.4128` n `422`
- 4h: commodity avg `0.3342` n `12`; crypto_alt avg `-1.239` n `228`; crypto_major avg `-1.6839` n `8`; equity avg `0.3684` n `69`; fx avg `-0.027` n `6`; index avg `0.121` n `23`; metal avg `-0.2224` n `18`; unknown avg `-0.6418` n `422`
- 24h: commodity avg `0.3585` n `12`; crypto_alt avg `-5.1378` n `228`; crypto_major avg `-6.3922` n `8`; equity avg `1.0326` n `69`; fx avg `0.0646` n `6`; index avg `0.7195` n `23`; metal avg `0.1512` n `18`; unknown avg `-0.8216` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
