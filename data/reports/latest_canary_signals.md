# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T02:52:27.716414+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `13`; crypto_alt avg `0.0157` n `239`; crypto_major avg `0.03` n `8`; equity avg `0.0529` n `162`; fx avg `0.0005` n `6`; index avg `0.0083` n `27`; metal avg `0.0031` n `20`; unknown avg `-0.2864` n `1264`
- 1h: commodity avg `-0.0453` n `13`; crypto_alt avg `0.0048` n `239`; crypto_major avg `-0.3506` n `8`; equity avg `0.0608` n `162`; fx avg `0.0019` n `6`; index avg `0.0011` n `27`; metal avg `0.0303` n `20`; unknown avg `-0.142` n `1264`
- 4h: commodity avg `-0.0922` n `13`; crypto_alt avg `-0.283` n `239`; crypto_major avg `-0.7362` n `8`; equity avg `0.2245` n `162`; fx avg `0.0359` n `6`; index avg `0.0279` n `27`; metal avg `0.1945` n `20`; unknown avg `41.421` n `1258`
- 24h: commodity avg `-0.9598` n `13`; crypto_alt avg `-0.5653` n `239`; crypto_major avg `-0.033` n `8`; equity avg `-3.003` n `162`; fx avg `-0.0543` n `6`; index avg `-0.2629` n `27`; metal avg `-0.0647` n `20`; unknown avg `563.036` n `999`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
