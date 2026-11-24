# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T21:07:30.006191+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `13`; crypto_alt avg `-0.284` n `239`; crypto_major avg `-0.2026` n `8`; equity avg `-0.3812` n `168`; fx avg `-0.0036` n `6`; index avg `-0.0423` n `27`; metal avg `-0.0321` n `20`; unknown avg `-0.1109` n `1237`
- 1h: commodity avg `0.0519` n `13`; crypto_alt avg `0.1246` n `239`; crypto_major avg `0.1755` n `8`; equity avg `0.2478` n `168`; fx avg `-0.0097` n `6`; index avg `0.0317` n `27`; metal avg `0.0035` n `20`; unknown avg `1.0401` n `1231`
- 4h: commodity avg `0.1352` n `13`; crypto_alt avg `-0.168` n `239`; crypto_major avg `-0.0008` n `8`; equity avg `0.2068` n `168`; fx avg `-0.0394` n `6`; index avg `0.0257` n `27`; metal avg `-0.0729` n `20`; unknown avg `381.4313` n `1201`
- 24h: commodity avg `0.646` n `13`; crypto_alt avg `-3.1812` n `239`; crypto_major avg `-3.0726` n `8`; equity avg `-4.214` n `167`; fx avg `0.2249` n `6`; index avg `-0.2855` n `27`; metal avg `-1.1302` n `20`; unknown avg `413.0583` n `1101`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
