# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T07:07:25.317880+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `13`; crypto_alt avg `0.0822` n `239`; crypto_major avg `0.0121` n `8`; equity avg `-0.0021` n `158`; fx avg `0.0007` n `6`; index avg `0.003` n `27`; metal avg `0.0085` n `20`; unknown avg `199.164` n `1256`
- 1h: commodity avg `0.0445` n `13`; crypto_alt avg `-0.0866` n `239`; crypto_major avg `-0.0314` n `8`; equity avg `0.0043` n `158`; fx avg `-0.002` n `6`; index avg `0.0012` n `27`; metal avg `0.0041` n `20`; unknown avg `200.716` n `1246`
- 4h: commodity avg `-0.0153` n `13`; crypto_alt avg `-0.2822` n `239`; crypto_major avg `-0.0799` n `8`; equity avg `-0.0163` n `158`; fx avg `0.0151` n `6`; index avg `-0.0011` n `27`; metal avg `-0.0064` n `20`; unknown avg `0.0358` n `1208`
- 24h: commodity avg `0.1023` n `13`; crypto_alt avg `-1.8422` n `239`; crypto_major avg `-0.6871` n `8`; equity avg `0.0713` n `158`; fx avg `0.0454` n `6`; index avg `0.0325` n `27`; metal avg `-0.0377` n `20`; unknown avg `158.8983` n `1081`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
