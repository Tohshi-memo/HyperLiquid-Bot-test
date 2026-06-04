# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T17:22:26.928985+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0349` n `12`; crypto_alt avg `-0.4023` n `228`; crypto_major avg `-0.412` n `8`; equity avg `-0.0243` n `74`; fx avg `-0.0023` n `6`; index avg `0.0756` n `23`; metal avg `-0.1515` n `18`; unknown avg `0.8618` n `424`
- 1h: commodity avg `-0.1282` n `12`; crypto_alt avg `-0.2822` n `228`; crypto_major avg `-0.4141` n `8`; equity avg `-0.0407` n `74`; fx avg `-0.0095` n `6`; index avg `0.148` n `23`; metal avg `-0.1181` n `18`; unknown avg `4.9464` n `424`
- 4h: commodity avg `-0.225` n `12`; crypto_alt avg `1.2665` n `228`; crypto_major avg `0.6009` n `8`; equity avg `0.9797` n `74`; fx avg `-0.0511` n `6`; index avg `0.8353` n `23`; metal avg `-0.5909` n `18`; unknown avg `5.1915` n `424`
- 24h: commodity avg `-1.0137` n `12`; crypto_alt avg `-4.9967` n `228`; crypto_major avg `-3.8048` n `8`; equity avg `-0.881` n `73`; fx avg `0.0787` n `6`; index avg `-0.0273` n `23`; metal avg `0.4786` n `18`; unknown avg `3.1364` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
