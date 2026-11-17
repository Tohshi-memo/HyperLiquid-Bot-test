# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T12:52:26.866905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0206` n `13`; crypto_alt avg `0.1173` n `239`; crypto_major avg `0.166` n `8`; equity avg `-0.3115` n `162`; fx avg `0.0149` n `6`; index avg `-0.0142` n `27`; metal avg `0.0307` n `20`; unknown avg `2.6558` n `1266`
- 1h: commodity avg `0.0221` n `13`; crypto_alt avg `0.2693` n `239`; crypto_major avg `0.3026` n `8`; equity avg `0.1462` n `162`; fx avg `0.0222` n `6`; index avg `-0.0101` n `27`; metal avg `-0.0412` n `20`; unknown avg `0.2262` n `1254`
- 4h: commodity avg `0.2618` n `13`; crypto_alt avg `0.8612` n `239`; crypto_major avg `0.7991` n `8`; equity avg `0.9098` n `162`; fx avg `0.0089` n `6`; index avg `0.0789` n `27`; metal avg `-0.0003` n `20`; unknown avg `19.5707` n `1256`
- 24h: commodity avg `-0.4804` n `13`; crypto_alt avg `2.5006` n `239`; crypto_major avg `2.5287` n `8`; equity avg `-0.8228` n `162`; fx avg `-0.018` n `6`; index avg `-0.1191` n `27`; metal avg `-0.1359` n `20`; unknown avg `8.6534` n `1115`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
