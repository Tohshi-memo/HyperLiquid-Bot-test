# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T13:31:35.067868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0248` n `13`; crypto_alt avg `0.205` n `239`; crypto_major avg `0.1533` n `8`; equity avg `0.0823` n `158`; fx avg `-0.0049` n `6`; index avg `0.0151` n `27`; metal avg `0.0059` n `20`; unknown avg `0.0425` n `1263`
- 1h: commodity avg `-0.0064` n `13`; crypto_alt avg `0.2247` n `239`; crypto_major avg `0.0814` n `8`; equity avg `0.1506` n `158`; fx avg `0.0029` n `6`; index avg `0.0207` n `27`; metal avg `0.0004` n `20`; unknown avg `0.7328` n `1255`
- 4h: commodity avg `0.0513` n `13`; crypto_alt avg `-0.2201` n `239`; crypto_major avg `-0.2069` n `8`; equity avg `0.0196` n `158`; fx avg `0.0527` n `6`; index avg `0.0022` n `27`; metal avg `0.0114` n `20`; unknown avg `-0.0467` n `1249`
- 24h: commodity avg `-0.1105` n `13`; crypto_alt avg `-1.216` n `239`; crypto_major avg `-0.3658` n `8`; equity avg `-0.1122` n `158`; fx avg `0.0403` n `6`; index avg `0.003` n `27`; metal avg `0.1418` n `20`; unknown avg `0.1391` n `1117`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
