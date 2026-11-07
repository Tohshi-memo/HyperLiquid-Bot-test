# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T03:07:26.459012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `13`; crypto_alt avg `0.0785` n `239`; crypto_major avg `0.1228` n `8`; equity avg `0.1038` n `158`; fx avg `0.0001` n `6`; index avg `-0.0055` n `27`; metal avg `0.0118` n `20`; unknown avg `0.166` n `1257`
- 1h: commodity avg `0.0262` n `13`; crypto_alt avg `-0.2368` n `239`; crypto_major avg `-0.0796` n `8`; equity avg `-0.1209` n `158`; fx avg `-0.0115` n `6`; index avg `-0.0079` n `27`; metal avg `0.0056` n `20`; unknown avg `0.1076` n `1255`
- 4h: commodity avg `-0.0522` n `13`; crypto_alt avg `0.1206` n `239`; crypto_major avg `0.3164` n `8`; equity avg `0.0243` n `158`; fx avg `-0.0125` n `6`; index avg `0.0091` n `27`; metal avg `0.0099` n `20`; unknown avg `0.2462` n `1247`
- 24h: commodity avg `-0.1268` n `13`; crypto_alt avg `0.3384` n `239`; crypto_major avg `-0.1803` n `8`; equity avg `0.6172` n `158`; fx avg `-0.1208` n `6`; index avg `0.074` n `27`; metal avg `0.121` n `20`; unknown avg `8.2411` n `1022`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
