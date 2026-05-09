# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T22:52:13.192987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0223` n `12`; crypto_alt avg `0.0694` n `228`; crypto_major avg `0.0637` n `8`; equity avg `-0.0` n `65`; fx avg `0.0008` n `5`; index avg `0.0068` n `23`; metal avg `0.0048` n `18`; unknown avg `-0.1143` n `376`
- 1h: commodity avg `-0.0436` n `12`; crypto_alt avg `0.0817` n `228`; crypto_major avg `0.0303` n `8`; equity avg `0.1352` n `65`; fx avg `0.0` n `5`; index avg `0.0252` n `23`; metal avg `0.0154` n `18`; unknown avg `-0.262` n `376`
- 4h: commodity avg `-0.0328` n `12`; crypto_alt avg `0.0728` n `228`; crypto_major avg `-0.0148` n `8`; equity avg `0.3548` n `65`; fx avg `-0.0066` n `5`; index avg `0.0833` n `23`; metal avg `0.1657` n `18`; unknown avg `-0.1403` n `376`
- 24h: commodity avg `0.4153` n `12`; crypto_alt avg `0.0184` n `228`; crypto_major avg `0.2436` n `8`; equity avg `0.7277` n `65`; fx avg `-0.0227` n `5`; index avg `0.3617` n `23`; metal avg `0.3011` n `18`; unknown avg `0.0689` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
