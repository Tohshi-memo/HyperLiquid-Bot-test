# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T16:52:32.629811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1178` n `12`; crypto_alt avg `-0.0078` n `230`; crypto_major avg `-0.1218` n `8`; equity avg `-0.2851` n `102`; fx avg `-0.0127` n `6`; index avg `-0.0844` n `25`; metal avg `-0.1061` n `20`; unknown avg `-0.2667` n `774`
- 1h: commodity avg `-0.0215` n `12`; crypto_alt avg `0.4108` n `230`; crypto_major avg `0.4299` n `8`; equity avg `0.5614` n `102`; fx avg `-0.0268` n `6`; index avg `0.0164` n `25`; metal avg `0.0345` n `20`; unknown avg `0.0801` n `774`
- 4h: commodity avg `-0.1656` n `12`; crypto_alt avg `-1.2473` n `230`; crypto_major avg `-1.0388` n `8`; equity avg `-2.3999` n `102`; fx avg `-0.0828` n `6`; index avg `-0.5811` n `25`; metal avg `-0.008` n `20`; unknown avg `-0.3342` n `774`
- 24h: commodity avg `-0.5853` n `12`; crypto_alt avg `-1.1876` n `230`; crypto_major avg `-0.5268` n `8`; equity avg `-1.6809` n `102`; fx avg `0.0155` n `6`; index avg `-0.5228` n `25`; metal avg `0.2388` n `20`; unknown avg `-0.4163` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1992`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
