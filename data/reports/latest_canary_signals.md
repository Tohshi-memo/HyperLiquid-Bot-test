# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T00:52:26.930152+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0864` n `13`; crypto_alt avg `-0.0553` n `239`; crypto_major avg `-0.0118` n `8`; equity avg `-0.0096` n `158`; fx avg `0.0007` n `6`; index avg `-0.0018` n `27`; metal avg `0.0016` n `20`; unknown avg `1.7988` n `1262`
- 1h: commodity avg `-0.0199` n `13`; crypto_alt avg `-0.3148` n `239`; crypto_major avg `-0.2107` n `8`; equity avg `-0.0623` n `158`; fx avg `0.0219` n `6`; index avg `0.0066` n `27`; metal avg `-0.0086` n `20`; unknown avg `0.0334` n `1250`
- 4h: commodity avg `-0.0688` n `13`; crypto_alt avg `0.363` n `239`; crypto_major avg `0.4284` n `8`; equity avg `0.0777` n `158`; fx avg `0.0088` n `6`; index avg `0.0114` n `27`; metal avg `0.001` n `20`; unknown avg `1.2984` n `1208`
- 24h: commodity avg `0.002` n `13`; crypto_alt avg `-1.631` n `239`; crypto_major avg `-0.7406` n `8`; equity avg `-0.0784` n `158`; fx avg `0.0062` n `6`; index avg `0.061` n `27`; metal avg `-0.0282` n `20`; unknown avg `160.9381` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
