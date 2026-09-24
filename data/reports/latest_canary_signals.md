# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T05:07:35.572490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0191` n `12`; crypto_alt avg `0.9225` n `234`; crypto_major avg `0.8504` n `8`; equity avg `0.2274` n `141`; fx avg `-0.0283` n `6`; index avg `0.0149` n `26`; metal avg `0.0427` n `20`; unknown avg `3.8697` n `943`
- 1h: commodity avg `0.001` n `12`; crypto_alt avg `1.3448` n `234`; crypto_major avg `1.0228` n `8`; equity avg `0.3108` n `141`; fx avg `-0.0209` n `6`; index avg `0.0357` n `26`; metal avg `0.0851` n `20`; unknown avg `2.3163` n `943`
- 4h: commodity avg `0.0451` n `12`; crypto_alt avg `1.9098` n `234`; crypto_major avg `0.5261` n `8`; equity avg `-0.1425` n `141`; fx avg `-0.0065` n `6`; index avg `-0.0384` n `26`; metal avg `0.0089` n `20`; unknown avg `2.1227` n `937`
- 24h: commodity avg `0.5064` n `12`; crypto_alt avg `-3.4574` n `234`; crypto_major avg `-3.7536` n `8`; equity avg `-1.7093` n `140`; fx avg `0.0939` n `6`; index avg `-0.3462` n `26`; metal avg `-0.6049` n `20`; unknown avg `584.6146` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
