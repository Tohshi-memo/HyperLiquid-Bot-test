# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T16:37:26.680144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1123` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0077` n `12`; crypto_alt avg `-0.2299` n `228`; crypto_major avg `-0.1486` n `8`; equity avg `-0.0333` n `74`; fx avg `0.0065` n `6`; index avg `0.0933` n `23`; metal avg `-0.0533` n `18`; unknown avg `0.9644` n `424`
- 1h: commodity avg `-0.0387` n `12`; crypto_alt avg `-0.3227` n `228`; crypto_major avg `-0.1578` n `8`; equity avg `-0.1601` n `74`; fx avg `0.0025` n `6`; index avg `0.1385` n `23`; metal avg `0.0491` n `18`; unknown avg `0.9815` n `424`
- 4h: commodity avg `0.0521` n `12`; crypto_alt avg `0.4917` n `228`; crypto_major avg `-0.3203` n `8`; equity avg `0.9189` n `74`; fx avg `-0.0316` n `6`; index avg `0.792` n `23`; metal avg `-0.3717` n `18`; unknown avg `0.8873` n `424`
- 24h: commodity avg `-0.8564` n `12`; crypto_alt avg `-4.7213` n `228`; crypto_major avg `-3.4179` n `8`; equity avg `-0.8737` n `73`; fx avg `0.0845` n `6`; index avg `-0.1019` n `23`; metal avg `0.6056` n `18`; unknown avg `-0.0644` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
