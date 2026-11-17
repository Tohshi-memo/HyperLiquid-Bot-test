# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T01:22:31.526736+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0334` n `13`; crypto_alt avg `-0.0531` n `239`; crypto_major avg `0.036` n `8`; equity avg `0.1174` n `162`; fx avg `0.0212` n `6`; index avg `-0.0003` n `27`; metal avg `-0.007` n `20`; unknown avg `9.4209` n `1264`
- 1h: commodity avg `-0.031` n `13`; crypto_alt avg `-0.1662` n `239`; crypto_major avg `0.2255` n `8`; equity avg `0.2626` n `162`; fx avg `0.0502` n `6`; index avg `0.0457` n `27`; metal avg `0.0133` n `20`; unknown avg `14.5844` n `1264`
- 4h: commodity avg `-0.078` n `13`; crypto_alt avg `-0.3899` n `239`; crypto_major avg `-0.1632` n `8`; equity avg `0.1375` n `162`; fx avg `0.0701` n `6`; index avg `0.0271` n `27`; metal avg `0.0428` n `20`; unknown avg `2.7337` n `1220`
- 24h: commodity avg `-0.9871` n `13`; crypto_alt avg `0.1411` n `239`; crypto_major avg `0.6073` n `8`; equity avg `-2.9711` n `162`; fx avg `-0.0587` n `6`; index avg `-0.2818` n `27`; metal avg `-0.3711` n `20`; unknown avg `513.5689` n `997`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
