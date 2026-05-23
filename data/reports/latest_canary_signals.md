# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T03:52:15.035565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `12`; crypto_alt avg `-0.0834` n `228`; crypto_major avg `0.1268` n `8`; equity avg `-0.0175` n `67`; fx avg `0.0` n `6`; index avg `0.0011` n `23`; metal avg `0.0117` n `18`; unknown avg `-0.0327` n `386`
- 1h: commodity avg `0.1822` n `12`; crypto_alt avg `0.3013` n `228`; crypto_major avg `0.2838` n `8`; equity avg `0.0106` n `67`; fx avg `-0.0007` n `6`; index avg `0.0532` n `23`; metal avg `0.0231` n `18`; unknown avg `0.043` n `386`
- 4h: commodity avg `0.1312` n `12`; crypto_alt avg `1.0315` n `228`; crypto_major avg `0.2729` n `8`; equity avg `-0.1672` n `67`; fx avg `-0.0049` n `6`; index avg `-0.0335` n `23`; metal avg `-0.0103` n `18`; unknown avg `-0.8941` n `386`
- 24h: commodity avg `0.116` n `12`; crypto_alt avg `-3.3007` n `228`; crypto_major avg `-2.3344` n `8`; equity avg `-1.7895` n `67`; fx avg `0.0593` n `6`; index avg `0.0149` n `23`; metal avg `-0.7792` n `18`; unknown avg `-1.9953` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
