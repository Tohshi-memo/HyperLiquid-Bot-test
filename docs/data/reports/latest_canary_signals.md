# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T22:03:12.641490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0063` n `13`; crypto_alt avg `0.0307` n `239`; crypto_major avg `-0.1156` n `8`; equity avg `0.0209` n `162`; fx avg `-0.0145` n `6`; index avg `-0.0035` n `27`; metal avg `0.0031` n `20`; unknown avg `1.7399` n `1249`
- 1h: commodity avg `-0.0259` n `13`; crypto_alt avg `-0.1827` n `239`; crypto_major avg `0.0377` n `8`; equity avg `0.0624` n `162`; fx avg `-0.0248` n `6`; index avg `-0.0163` n `27`; metal avg `-0.013` n `20`; unknown avg `3.3037` n `1251`
- 4h: commodity avg `0.0021` n `13`; crypto_alt avg `0.5274` n `239`; crypto_major avg `0.7292` n `8`; equity avg `0.5734` n `162`; fx avg `0.0377` n `6`; index avg `0.0437` n `27`; metal avg `0.0728` n `20`; unknown avg `43.4426` n `1225`
- 24h: commodity avg `0.0402` n `13`; crypto_alt avg `3.2967` n `239`; crypto_major avg `4.1502` n `8`; equity avg `1.3139` n `162`; fx avg `0.0225` n `6`; index avg `0.1021` n `27`; metal avg `0.2797` n `20`; unknown avg `4.6073` n `1150`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
