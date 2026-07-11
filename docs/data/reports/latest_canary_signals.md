# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T02:37:25.917472+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `0.0907` n `229`; crypto_major avg `0.1047` n `8`; equity avg `0.0124` n `92`; fx avg `0.0012` n `6`; index avg `0.0095` n `25`; metal avg `0.004` n `20`; unknown avg `-0.012` n `765`
- 1h: commodity avg `-0.0398` n `12`; crypto_alt avg `-0.1057` n `229`; crypto_major avg `-0.2135` n `8`; equity avg `0.0046` n `92`; fx avg `0.001` n `6`; index avg `-0.0018` n `25`; metal avg `-0.0097` n `20`; unknown avg `-0.0767` n `765`
- 4h: commodity avg `-0.0573` n `12`; crypto_alt avg `-0.0168` n `229`; crypto_major avg `-0.1627` n `8`; equity avg `0.0861` n `92`; fx avg `0.028` n `6`; index avg `-0.0181` n `25`; metal avg `0.0043` n `20`; unknown avg `3.1496` n `765`
- 24h: commodity avg `-0.3935` n `12`; crypto_alt avg `0.394` n `229`; crypto_major avg `-0.1462` n `8`; equity avg `-0.7046` n `92`; fx avg `-0.172` n `6`; index avg `0.0542` n `25`; metal avg `0.0107` n `20`; unknown avg `4.114` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
