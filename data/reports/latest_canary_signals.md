# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T09:37:35.115779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0082` n `12`; crypto_alt avg `0.0484` n `228`; crypto_major avg `-0.052` n `8`; equity avg `0.0086` n `86`; fx avg `0.0146` n `6`; index avg `0.0118` n `23`; metal avg `0.1047` n `20`; unknown avg `-0.0651` n `765`
- 1h: commodity avg `-0.0076` n `12`; crypto_alt avg `-0.0441` n `228`; crypto_major avg `-0.2791` n `8`; equity avg `-0.2347` n `86`; fx avg `-0.0081` n `6`; index avg `-0.0517` n `23`; metal avg `0.212` n `20`; unknown avg `-0.079` n `765`
- 4h: commodity avg `-0.2509` n `12`; crypto_alt avg `0.6787` n `228`; crypto_major avg `0.5657` n `8`; equity avg `-0.0393` n `86`; fx avg `-0.0128` n `6`; index avg `-0.02` n `23`; metal avg `0.6877` n `20`; unknown avg `0.0691` n `733`
- 24h: commodity avg `-0.0077` n `12`; crypto_alt avg `-1.5646` n `228`; crypto_major avg `-1.8431` n `8`; equity avg `-4.0475` n `86`; fx avg `0.0142` n `6`; index avg `-0.5972` n `23`; metal avg `0.6207` n `20`; unknown avg `0.8124` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2621`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
