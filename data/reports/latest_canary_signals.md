# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T22:07:25.954449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `12`; crypto_alt avg `-0.0701` n `231`; crypto_major avg `0.0083` n `8`; equity avg `0.003` n `128`; fx avg `0.0034` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0014` n `20`; unknown avg `-0.141` n `784`
- 1h: commodity avg `0.0047` n `12`; crypto_alt avg `0.0088` n `231`; crypto_major avg `0.0042` n `8`; equity avg `0.016` n `128`; fx avg `0.0015` n `6`; index avg `-0.0046` n `26`; metal avg `0.0009` n `20`; unknown avg `-0.079` n `774`
- 4h: commodity avg `-0.0118` n `12`; crypto_alt avg `0.2367` n `231`; crypto_major avg `0.1431` n `8`; equity avg `0.1906` n `128`; fx avg `-0.0171` n `6`; index avg `0.0342` n `26`; metal avg `0.0181` n `20`; unknown avg `0.1521` n `774`
- 24h: commodity avg `-0.0432` n `12`; crypto_alt avg `0.8729` n `231`; crypto_major avg `1.1856` n `8`; equity avg `0.4126` n `128`; fx avg `-0.0472` n `6`; index avg `0.079` n `26`; metal avg `0.1246` n `20`; unknown avg `4952.6602` n `742`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2029`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.059`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0572`, n `668`, weak_sample_signal
