# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T13:22:27.502381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0533` n `13`; crypto_alt avg `-0.0877` n `239`; crypto_major avg `-0.1212` n `8`; equity avg `-0.2883` n `162`; fx avg `-0.0109` n `6`; index avg `-0.0381` n `27`; metal avg `-0.1168` n `20`; unknown avg `0.41` n `1228`
- 1h: commodity avg `0.115` n `13`; crypto_alt avg `0.2892` n `239`; crypto_major avg `0.4016` n `8`; equity avg `-0.3246` n `162`; fx avg `-0.0039` n `6`; index avg `-0.039` n `27`; metal avg `-0.1384` n `20`; unknown avg `0.4274` n `1224`
- 4h: commodity avg `0.3119` n `13`; crypto_alt avg `1.4736` n `239`; crypto_major avg `1.3518` n `8`; equity avg `1.7599` n `162`; fx avg `0.0157` n `6`; index avg `0.1493` n `27`; metal avg `-0.0071` n `20`; unknown avg `1.1255` n `1216`
- 24h: commodity avg `-0.3788` n `13`; crypto_alt avg `2.5696` n `239`; crypto_major avg `2.5407` n `8`; equity avg `-0.8597` n `162`; fx avg `-0.0718` n `6`; index avg `-0.1282` n `27`; metal avg `-0.1871` n `20`; unknown avg `11.856` n `1105`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
