# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T02:07:22.996421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `13`; crypto_alt avg `0.0058` n `239`; crypto_major avg `0.0098` n `8`; equity avg `-0.0762` n `158`; fx avg `0.0074` n `6`; index avg `-0.0059` n `27`; metal avg `-0.0064` n `20`; unknown avg `-0.0366` n `1257`
- 1h: commodity avg `-0.0575` n `13`; crypto_alt avg `-0.0724` n `239`; crypto_major avg `0.1187` n `8`; equity avg `-0.124` n `158`; fx avg `0.0047` n `6`; index avg `-0.0208` n `27`; metal avg `-0.001` n `20`; unknown avg `2.2195` n `1255`
- 4h: commodity avg `-0.0609` n `13`; crypto_alt avg `-0.1345` n `239`; crypto_major avg `0.0817` n `8`; equity avg `-0.0129` n `158`; fx avg `0.008` n `6`; index avg `-0.0062` n `27`; metal avg `0.0132` n `20`; unknown avg `-0.0436` n `1233`
- 24h: commodity avg `-0.0823` n `13`; crypto_alt avg `1.12` n `239`; crypto_major avg `0.0796` n `8`; equity avg `1.3955` n `158`; fx avg `-0.0749` n `6`; index avg `0.184` n `27`; metal avg `0.1105` n `20`; unknown avg `8.3687` n `1024`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
