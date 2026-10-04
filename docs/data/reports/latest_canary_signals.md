# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T21:22:26.787180+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0525` n `13`; crypto_alt avg `0.0043` n `235`; crypto_major avg `0.1073` n `8`; equity avg `0.0231` n `144`; fx avg `-0.0008` n `6`; index avg `-0.0043` n `26`; metal avg `-0.0061` n `20`; unknown avg `0.0034` n `1068`
- 1h: commodity avg `-0.0627` n `13`; crypto_alt avg `-0.1349` n `235`; crypto_major avg `0.332` n `8`; equity avg `0.0707` n `144`; fx avg `-0.0047` n `6`; index avg `0.0069` n `26`; metal avg `0.0008` n `20`; unknown avg `9.5761` n `1062`
- 4h: commodity avg `-0.0423` n `13`; crypto_alt avg `0.3461` n `235`; crypto_major avg `0.5211` n `8`; equity avg `0.1055` n `144`; fx avg `-0.0101` n `6`; index avg `0.0173` n `26`; metal avg `0.0111` n `20`; unknown avg `2.9664` n `1050`
- 24h: commodity avg `-0.1493` n `13`; crypto_alt avg `0.8314` n `235`; crypto_major avg `1.4065` n `8`; equity avg `0.2654` n `144`; fx avg `0.0115` n `6`; index avg `-0.0037` n `26`; metal avg `0.0045` n `20`; unknown avg `1.5134` n `1010`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
