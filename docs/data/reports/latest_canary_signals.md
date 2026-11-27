# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T20:52:28.404240+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `13`; crypto_alt avg `-0.0574` n `239`; crypto_major avg `-0.0166` n `8`; equity avg `-0.018` n `168`; fx avg `-0.0085` n `6`; index avg `0.0269` n `27`; metal avg `0.0142` n `20`; unknown avg `28.7515` n `1265`
- 1h: commodity avg `0.0121` n `13`; crypto_alt avg `0.0454` n `239`; crypto_major avg `-0.0427` n `8`; equity avg `0.1037` n `168`; fx avg `-0.0081` n `6`; index avg `0.054` n `27`; metal avg `0.0541` n `20`; unknown avg `28.946` n `1251`
- 4h: commodity avg `0.0694` n `13`; crypto_alt avg `-0.0804` n `239`; crypto_major avg `-0.444` n `8`; equity avg `0.2735` n `168`; fx avg `-0.0183` n `6`; index avg `0.0687` n `27`; metal avg `0.2093` n `20`; unknown avg `193.4131` n `1236`
- 24h: commodity avg `-0.477` n `13`; crypto_alt avg `-0.0832` n `239`; crypto_major avg `-0.1278` n `8`; equity avg `3.2266` n `168`; fx avg `-0.1576` n `6`; index avg `0.3545` n `27`; metal avg `0.9541` n `20`; unknown avg `287.2564` n `1045`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
