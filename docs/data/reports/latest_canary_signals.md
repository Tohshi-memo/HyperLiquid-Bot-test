# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T18:37:26.967905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.4` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-2.1321` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7538` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.7439` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1024` n `12`; crypto_alt avg `-0.1927` n `228`; crypto_major avg `-0.2622` n `8`; equity avg `-0.127` n `69`; fx avg `0.0049` n `6`; index avg `0.0045` n `23`; metal avg `-0.0075` n `18`; unknown avg `1.2803` n `422`
- 1h: commodity avg `0.0447` n `12`; crypto_alt avg `-1.0821` n `228`; crypto_major avg `-0.7714` n `8`; equity avg `-0.1039` n `69`; fx avg `-0.0208` n `6`; index avg `0.0469` n `23`; metal avg `0.0219` n `18`; unknown avg `0.7162` n `422`
- 4h: commodity avg `0.6216` n `12`; crypto_alt avg `-0.9216` n `228`; crypto_major avg `-1.5105` n `8`; equity avg `0.2334` n `69`; fx avg `-0.0565` n `6`; index avg `0.2433` n `23`; metal avg `-0.2941` n `18`; unknown avg `1.0601` n `422`
- 24h: commodity avg `0.1426` n `12`; crypto_alt avg `-3.8318` n `228`; crypto_major avg `-4.3168` n `8`; equity avg `-0.1669` n `69`; fx avg `0.0526` n `6`; index avg `-0.0218` n `23`; metal avg `0.1744` n `18`; unknown avg `-0.1322` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
