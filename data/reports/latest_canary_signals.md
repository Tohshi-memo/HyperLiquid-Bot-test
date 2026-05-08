# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T09:37:13.727450+00:00`
- Correlation status: `ready`
- Asset price records: `634`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0842` n `12`; crypto_alt avg `-0.2119` n `228`; crypto_major avg `-0.1333` n `8`; equity avg `-0.0973` n `65`; fx avg `-0.0033` n `5`; index avg `-0.0606` n `23`; metal avg `-0.1078` n `18`; unknown avg `-0.2038` n `375`
- 1h: commodity avg `0.0268` n `12`; crypto_alt avg `0.2699` n `228`; crypto_major avg `0.1504` n `8`; equity avg `0.1116` n `65`; fx avg `0.0135` n `5`; index avg `0.0202` n `23`; metal avg `-0.0469` n `18`; unknown avg `0.0172` n `375`
- 4h: commodity avg `-0.1564` n `12`; crypto_alt avg `0.3756` n `228`; crypto_major avg `0.2805` n `8`; equity avg `0.686` n `65`; fx avg `0.0696` n `5`; index avg `0.1884` n `23`; metal avg `-0.0395` n `18`; unknown avg `0.401` n `355`
- 24h: commodity avg `1.2351` n `12`; crypto_alt avg `1.0862` n `228`; crypto_major avg `-1.5114` n `8`; equity avg `-0.6616` n `65`; fx avg `0.2304` n `5`; index avg `-0.4495` n `23`; metal avg `-0.5055` n `18`; unknown avg `-0.0749` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1361`, n `626`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1353`, n `626`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1117`, n `630`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0981`, n `630`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0948`, n `630`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `630`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0868`, n `626`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0844`, n `626`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `630`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `630`, weak_sample_signal
