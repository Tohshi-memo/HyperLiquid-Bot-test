# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T16:52:29.325982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_equity_divergence: score `-5.4706` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `-5.4706` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `-5.1129` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `-5.1129` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `4.9977` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `4.9977` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `-0.3339` n `228`; crypto_major avg `-0.3517` n `8`; equity avg `-0.0995` n `78`; fx avg `0.0069` n `6`; index avg `-0.0072` n `23`; metal avg `0.1314` n `18`; unknown avg `-0.0169` n `687`
- 1h: commodity avg `0.3836` n `12`; crypto_alt avg `-3.5111` n `228`; crypto_major avg `-4.7293` n `8`; equity avg `0.7413` n `78`; fx avg `-0.1148` n `6`; index avg `0.2684` n `23`; metal avg `-4.2752` n `18`; unknown avg `-0.4305` n `572`
- 4h: commodity avg `0.3836` n `12`; crypto_alt avg `-3.5111` n `228`; crypto_major avg `-4.7293` n `8`; equity avg `0.7413` n `78`; fx avg `-0.1148` n `6`; index avg `0.2684` n `23`; metal avg `-4.2752` n `18`; unknown avg `-0.4305` n `572`
- 24h: commodity avg `0.3836` n `12`; crypto_alt avg `-3.5111` n `228`; crypto_major avg `-4.7293` n `8`; equity avg `0.7413` n `78`; fx avg `-0.1148` n `6`; index avg `0.2684` n `23`; metal avg `-4.2752` n `18`; unknown avg `-0.4305` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0715`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0673`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0631`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `669`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0618`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0596`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.054`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0524`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0507`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0496`, n `669`, weak_sample_signal
