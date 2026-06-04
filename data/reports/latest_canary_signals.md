# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T18:07:24.673928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.0963` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.7842` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1044` n `12`; crypto_alt avg `-0.5897` n `228`; crypto_major avg `-0.5569` n `8`; equity avg `-0.033` n `74`; fx avg `-0.0031` n `6`; index avg `0.0283` n `23`; metal avg `-0.0575` n `18`; unknown avg `-0.1769` n `424`
- 1h: commodity avg `0.0738` n `12`; crypto_alt avg `-0.8196` n `228`; crypto_major avg `-0.6594` n `8`; equity avg `0.1866` n `74`; fx avg `-0.0125` n `6`; index avg `0.2274` n `23`; metal avg `-0.0968` n `18`; unknown avg `0.5508` n `424`
- 4h: commodity avg `-0.0221` n `12`; crypto_alt avg `-0.3323` n `228`; crypto_major avg `-1.0049` n `8`; equity avg `0.7793` n `74`; fx avg `-0.0388` n `6`; index avg `1.0914` n `23`; metal avg `-0.1226` n `18`; unknown avg `1.4584` n `424`
- 24h: commodity avg `-0.6573` n `12`; crypto_alt avg `-5.9179` n `228`; crypto_major avg `-4.5686` n `8`; equity avg `-1.0603` n `73`; fx avg `0.0547` n `6`; index avg `0.026` n `23`; metal avg `0.684` n `18`; unknown avg `1.0812` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
