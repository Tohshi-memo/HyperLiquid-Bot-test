# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T10:22:27.778736+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `13`; crypto_alt avg `-0.1594` n `239`; crypto_major avg `-0.0642` n `8`; equity avg `-0.0434` n `158`; fx avg `0.0006` n `6`; index avg `0.0017` n `27`; metal avg `0.0005` n `20`; unknown avg `0.0768` n `1262`
- 1h: commodity avg `0.0386` n `13`; crypto_alt avg `0.1126` n `239`; crypto_major avg `0.0535` n `8`; equity avg `0.1231` n `158`; fx avg `-0.0076` n `6`; index avg `0.0171` n `27`; metal avg `-0.0083` n `20`; unknown avg `218.4873` n `1176`
- 4h: commodity avg `0.0628` n `13`; crypto_alt avg `-0.4302` n `239`; crypto_major avg `-0.2104` n `8`; equity avg `0.1791` n `158`; fx avg `-0.0017` n `6`; index avg `0.0033` n `27`; metal avg `0.0144` n `20`; unknown avg `221.8122` n `1156`
- 24h: commodity avg `0.0997` n `13`; crypto_alt avg `-1.539` n `239`; crypto_major avg `-0.6809` n `8`; equity avg `0.1568` n `158`; fx avg `0.05` n `6`; index avg `0.04` n `27`; metal avg `-0.0413` n `20`; unknown avg `5.6193` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
