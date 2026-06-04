# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T17:37:25.613424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3559` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1153` n `12`; crypto_alt avg `-0.2854` n `228`; crypto_major avg `-0.3095` n `8`; equity avg `0.137` n `74`; fx avg `-0.0078` n `6`; index avg `0.0556` n `23`; metal avg `0.1694` n `18`; unknown avg `-0.2103` n `424`
- 1h: commodity avg `-0.2358` n `12`; crypto_alt avg `-0.3372` n `228`; crypto_major avg `-0.574` n `8`; equity avg `0.1323` n `74`; fx avg `-0.0239` n `6`; index avg `0.1105` n `23`; metal avg `0.1045` n `18`; unknown avg `1.575` n `424`
- 4h: commodity avg `-0.2517` n `12`; crypto_alt avg `0.0243` n `228`; crypto_major avg `-0.723` n `8`; equity avg `0.5909` n `74`; fx avg `-0.0367` n `6`; index avg `0.6329` n `23`; metal avg `-0.4239` n `18`; unknown avg `2.5779` n `424`
- 24h: commodity avg `-1.0667` n `12`; crypto_alt avg `-5.8668` n `228`; crypto_major avg `-4.7254` n `8`; equity avg `-1.0357` n `73`; fx avg `0.0933` n `6`; index avg `0.0171` n `23`; metal avg `0.7156` n `18`; unknown avg `0.2506` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
