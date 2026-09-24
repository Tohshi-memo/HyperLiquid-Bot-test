# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T01:22:34.229199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0199` n `12`; crypto_alt avg `-0.2973` n `234`; crypto_major avg `-0.2498` n `8`; equity avg `-0.0726` n `141`; fx avg `-0.0129` n `6`; index avg `-0.0017` n `26`; metal avg `-0.0477` n `20`; unknown avg `0.5339` n `945`
- 1h: commodity avg `-0.0455` n `12`; crypto_alt avg `-0.2689` n `234`; crypto_major avg `-0.2904` n `8`; equity avg `-0.0945` n `141`; fx avg `0.0052` n `6`; index avg `0.0138` n `26`; metal avg `0.0565` n `20`; unknown avg `0.5173` n `943`
- 4h: commodity avg `-0.1901` n `12`; crypto_alt avg `0.2538` n `234`; crypto_major avg `0.3468` n `8`; equity avg `-0.125` n `141`; fx avg `0.005` n `6`; index avg `-0.0142` n `26`; metal avg `-0.044` n `20`; unknown avg `-0.1163` n `937`
- 24h: commodity avg `0.2972` n `12`; crypto_alt avg `-4.9026` n `234`; crypto_major avg `-3.9865` n `8`; equity avg `-1.79` n `140`; fx avg `0.0638` n `6`; index avg `-0.3304` n `26`; metal avg `-0.7136` n `20`; unknown avg `582.9856` n `821`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
