# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T07:22:25.452971+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.023` n `13`; crypto_alt avg `0.089` n `239`; crypto_major avg `0.0323` n `8`; equity avg `0.0032` n `158`; fx avg `0.0021` n `6`; index avg `0.0011` n `27`; metal avg `-0.0028` n `20`; unknown avg `0.0232` n `1262`
- 1h: commodity avg `0.059` n `13`; crypto_alt avg `-0.1008` n `239`; crypto_major avg `-0.0611` n `8`; equity avg `0.0187` n `158`; fx avg `0.0022` n `6`; index avg `0.0041` n `27`; metal avg `0.0101` n `20`; unknown avg `199.9006` n `1250`
- 4h: commodity avg `0.0282` n `13`; crypto_alt avg `-0.1259` n `239`; crypto_major avg `-0.0209` n `8`; equity avg `0.0074` n `158`; fx avg `0.0113` n `6`; index avg `-0.005` n `27`; metal avg `-0.0048` n `20`; unknown avg `0.1164` n `1208`
- 24h: commodity avg `0.1527` n `13`; crypto_alt avg `-1.8465` n `239`; crypto_major avg `-0.7087` n `8`; equity avg `0.0606` n `158`; fx avg `0.0469` n `6`; index avg `0.0308` n `27`; metal avg `-0.0418` n `20`; unknown avg `158.5716` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
