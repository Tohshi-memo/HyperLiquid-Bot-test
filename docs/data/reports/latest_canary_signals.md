# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T13:52:24.795692+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0247` n `13`; crypto_alt avg `0.005` n `239`; crypto_major avg `-0.0731` n `8`; equity avg `-0.152` n `160`; fx avg `0.0044` n `6`; index avg `-0.0118` n `27`; metal avg `0.0025` n `20`; unknown avg `0.0257` n `1264`
- 1h: commodity avg `-0.1896` n `13`; crypto_alt avg `-0.1723` n `239`; crypto_major avg `-0.4699` n `8`; equity avg `-0.9294` n `160`; fx avg `-0.0004` n `6`; index avg `-0.0818` n `27`; metal avg `-0.0458` n `20`; unknown avg `18.7621` n `1256`
- 4h: commodity avg `-0.0142` n `13`; crypto_alt avg `-0.4331` n `239`; crypto_major avg `-1.0459` n `8`; equity avg `-2.1732` n `160`; fx avg `0.0017` n `6`; index avg `-0.1676` n `27`; metal avg `-0.1407` n `20`; unknown avg `0.9235` n `1250`
- 24h: commodity avg `-0.7019` n `13`; crypto_alt avg `-0.5655` n `239`; crypto_major avg `-1.1201` n `8`; equity avg `1.3891` n `160`; fx avg `-0.0415` n `6`; index avg `0.2107` n `27`; metal avg `-0.2423` n `20`; unknown avg `2.1735` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
