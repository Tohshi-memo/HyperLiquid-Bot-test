# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T00:07:34.607858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0325` n `13`; crypto_alt avg `-0.0923` n `235`; crypto_major avg `-0.16` n `8`; equity avg `0.0075` n `150`; fx avg `0.0022` n `6`; index avg `0.0004` n `26`; metal avg `-0.0187` n `20`; unknown avg `0.1447` n `1068`
- 1h: commodity avg `0.0784` n `13`; crypto_alt avg `-0.0692` n `235`; crypto_major avg `-0.0275` n `8`; equity avg `-0.0028` n `150`; fx avg `0.0167` n `6`; index avg `-0.0098` n `26`; metal avg `-0.001` n `20`; unknown avg `-0.0065` n `1068`
- 4h: commodity avg `0.1057` n `13`; crypto_alt avg `-0.1127` n `235`; crypto_major avg `-0.1325` n `8`; equity avg `0.107` n `150`; fx avg `0.0121` n `6`; index avg `0.0168` n `26`; metal avg `-0.0278` n `20`; unknown avg `0.1513` n `998`
- 24h: commodity avg `0.4098` n `13`; crypto_alt avg `-1.448` n `235`; crypto_major avg `-0.9734` n `8`; equity avg `0.3952` n `149`; fx avg `0.0816` n `6`; index avg `0.0098` n `26`; metal avg `0.0739` n `20`; unknown avg `870.7165` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
