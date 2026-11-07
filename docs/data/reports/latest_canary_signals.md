# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T03:37:27.830398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0642` n `13`; crypto_alt avg `-0.2409` n `239`; crypto_major avg `-0.201` n `8`; equity avg `-0.0265` n `158`; fx avg `0.0003` n `6`; index avg `0.0064` n `27`; metal avg `-0.0051` n `20`; unknown avg `32.3095` n `1257`
- 1h: commodity avg `-0.0403` n `13`; crypto_alt avg `-0.4684` n `239`; crypto_major avg `-0.4034` n `8`; equity avg `0.0059` n `158`; fx avg `-0.0126` n `6`; index avg `0.0022` n `27`; metal avg `-0.0015` n `20`; unknown avg `15.6944` n `1249`
- 4h: commodity avg `-0.0975` n `13`; crypto_alt avg `-0.3628` n `239`; crypto_major avg `-0.2657` n `8`; equity avg `0.1357` n `158`; fx avg `-0.017` n `6`; index avg `0.0191` n `27`; metal avg `0.0209` n `20`; unknown avg `2.2554` n `1243`
- 24h: commodity avg `-0.3583` n `13`; crypto_alt avg `0.3302` n `239`; crypto_major avg `-0.0075` n `8`; equity avg `1.1712` n `158`; fx avg `-0.093` n `6`; index avg `0.1433` n `27`; metal avg `0.2312` n `20`; unknown avg `8.0238` n `1016`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
