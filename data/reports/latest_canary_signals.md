# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T17:52:14.795444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1785` n `12`; crypto_alt avg `-0.0766` n `228`; crypto_major avg `-0.0015` n `8`; equity avg `0.0276` n `67`; fx avg `0.0037` n `6`; index avg `-0.0143` n `23`; metal avg `-0.0748` n `18`; unknown avg `-0.0144` n `405`
- 1h: commodity avg `0.0266` n `12`; crypto_alt avg `-0.0848` n `228`; crypto_major avg `-0.274` n `8`; equity avg `0.0588` n `67`; fx avg `0.0064` n `6`; index avg `0.0901` n `23`; metal avg `-0.0595` n `18`; unknown avg `0.2414` n `405`
- 4h: commodity avg `-0.6715` n `12`; crypto_alt avg `0.8362` n `228`; crypto_major avg `-0.1152` n `8`; equity avg `0.1631` n `67`; fx avg `-0.0244` n `6`; index avg `0.1151` n `23`; metal avg `0.5602` n `18`; unknown avg `0.9877` n `405`
- 24h: commodity avg `-1.1611` n `12`; crypto_alt avg `2.157` n `228`; crypto_major avg `0.4377` n `8`; equity avg `0.8831` n `67`; fx avg `-0.0356` n `6`; index avg `0.5311` n `23`; metal avg `1.5508` n `18`; unknown avg `2.0218` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
