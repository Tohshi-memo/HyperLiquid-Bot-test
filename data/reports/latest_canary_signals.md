# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T01:52:14.461391+00:00`
- Correlation status: `ready`
- Asset price records: `603`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.066` n `12`; crypto_alt avg `-0.0484` n `228`; crypto_major avg `-0.0056` n `8`; equity avg `0.0057` n `65`; fx avg `-0.0089` n `5`; index avg `0.0048` n `23`; metal avg `0.1769` n `18`; unknown avg `-0.024` n `365`
- 1h: commodity avg `-0.3948` n `12`; crypto_alt avg `-0.046` n `228`; crypto_major avg `-0.1137` n `8`; equity avg `0.2345` n `65`; fx avg `-0.0007` n `5`; index avg `0.1551` n `23`; metal avg `0.7162` n `18`; unknown avg `0.1542` n `365`
- 4h: commodity avg `-0.5886` n `12`; crypto_alt avg `0.0373` n `228`; crypto_major avg `-0.3225` n `8`; equity avg `1.0845` n `65`; fx avg `0.1071` n `5`; index avg `0.5935` n `23`; metal avg `0.9934` n `18`; unknown avg `-0.24` n `365`
- 24h: commodity avg `0.5729` n `12`; crypto_alt avg `1.8992` n `228`; crypto_major avg `-1.4459` n `8`; equity avg `-0.8001` n `65`; fx avg `0.2105` n `5`; index avg `-0.571` n `23`; metal avg `-0.0017` n `18`; unknown avg `-0.3464` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1315`, n `599`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1173`, n `599`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.112`, n `599`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1084`, n `599`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1078`, n `595`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1061`, n `595`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0904`, n `595`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `595`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0779`, n `595`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0728`, n `599`, weak_sample_signal
