# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T11:52:28.273211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0189` n `13`; crypto_alt avg `0.0402` n `239`; crypto_major avg `0.0532` n `8`; equity avg `-0.0096` n `158`; fx avg `-0.0052` n `6`; index avg `-0.0074` n `27`; metal avg `0.0015` n `20`; unknown avg `0.6184` n `1262`
- 1h: commodity avg `0.0294` n `13`; crypto_alt avg `0.2215` n `239`; crypto_major avg `0.2766` n `8`; equity avg `0.0757` n `158`; fx avg `0.0007` n `6`; index avg `-0.0056` n `27`; metal avg `-0.0013` n `20`; unknown avg `0.523` n `1256`
- 4h: commodity avg `0.0039` n `13`; crypto_alt avg `-0.1259` n `239`; crypto_major avg `0.0313` n `8`; equity avg `0.1388` n `158`; fx avg `0.0032` n `6`; index avg `-0.0354` n `27`; metal avg `0.0049` n `20`; unknown avg `364.7629` n `1160`
- 24h: commodity avg `0.0616` n `13`; crypto_alt avg `-1.1742` n `239`; crypto_major avg `-0.3316` n `8`; equity avg `0.2165` n `158`; fx avg `0.0449` n `6`; index avg `0.0352` n `27`; metal avg `-0.0306` n `20`; unknown avg `5.4861` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
