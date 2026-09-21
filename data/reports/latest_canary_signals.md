# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T14:07:39.184256+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0952` n `12`; crypto_alt avg `-0.83` n `234`; crypto_major avg `-0.7284` n `8`; equity avg `-0.0376` n `140`; fx avg `-0.0065` n `6`; index avg `-0.0178` n `26`; metal avg `-0.0984` n `20`; unknown avg `0.888` n `898`
- 1h: commodity avg `-0.0594` n `12`; crypto_alt avg `-1.2239` n `234`; crypto_major avg `-0.6011` n `8`; equity avg `0.1136` n `140`; fx avg `-0.0101` n `6`; index avg `0.0319` n `26`; metal avg `-0.2041` n `20`; unknown avg `10.5151` n `898`
- 4h: commodity avg `-0.227` n `12`; crypto_alt avg `0.1453` n `234`; crypto_major avg `0.3862` n `8`; equity avg `0.1825` n `140`; fx avg `0.0069` n `6`; index avg `0.0474` n `26`; metal avg `0.0243` n `20`; unknown avg `11.0783` n `868`
- 24h: commodity avg `-0.8997` n `12`; crypto_alt avg `6.0839` n `234`; crypto_major avg `5.4063` n `8`; equity avg `2.1702` n `140`; fx avg `-0.0725` n `6`; index avg `0.402` n `26`; metal avg `0.0478` n `20`; unknown avg `3.0427` n `711`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
