# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T17:07:24.525959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0979` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3534` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0307` n `12`; crypto_alt avg `-0.3994` n `228`; crypto_major avg `-0.3199` n `8`; equity avg `-0.1168` n `73`; fx avg `-0.0102` n `6`; index avg `0.0658` n `23`; metal avg `0.1834` n `18`; unknown avg `-0.362` n `419`
- 1h: commodity avg `-0.0192` n `12`; crypto_alt avg `-0.6554` n `228`; crypto_major avg `-0.6335` n `8`; equity avg `-0.3327` n `73`; fx avg `-0.0128` n `6`; index avg `-0.0502` n `23`; metal avg `0.0965` n `18`; unknown avg `-0.2594` n `419`
- 4h: commodity avg `0.1962` n `12`; crypto_alt avg `-1.3854` n `228`; crypto_major avg `-1.9017` n `8`; equity avg `-2.2436` n `73`; fx avg `-0.0053` n `6`; index avg `-0.5483` n `23`; metal avg `-0.986` n `18`; unknown avg `-0.1776` n `419`
- 24h: commodity avg `0.9129` n `12`; crypto_alt avg `-0.3767` n `228`; crypto_major avg `-3.1369` n `8`; equity avg `-2.357` n `72`; fx avg `0.0271` n `6`; index avg `-0.2494` n `23`; metal avg `-1.8492` n `18`; unknown avg `-0.055` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0504`, n `668`, weak_sample_signal
