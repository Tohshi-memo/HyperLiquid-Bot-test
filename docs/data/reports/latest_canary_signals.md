# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T10:22:33.022060+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0265` n `13`; crypto_alt avg `-0.0555` n `239`; crypto_major avg `-0.1981` n `8`; equity avg `-0.2015` n `160`; fx avg `-0.0038` n `6`; index avg `-0.0132` n `27`; metal avg `-0.0199` n `20`; unknown avg `0.6591` n `1262`
- 1h: commodity avg `-0.1209` n `13`; crypto_alt avg `-0.3781` n `239`; crypto_major avg `-0.2668` n `8`; equity avg `-0.0049` n `160`; fx avg `-0.0244` n `6`; index avg `-0.0044` n `27`; metal avg `-0.0503` n `20`; unknown avg `32.9236` n `1256`
- 4h: commodity avg `-0.4193` n `13`; crypto_alt avg `-0.2847` n `239`; crypto_major avg `-0.7326` n `8`; equity avg `-0.0299` n `160`; fx avg `-0.0229` n `6`; index avg `-0.0359` n `27`; metal avg `-0.2691` n `20`; unknown avg `20.3066` n `1217`
- 24h: commodity avg `-0.8621` n `13`; crypto_alt avg `0.7653` n `239`; crypto_major avg `0.1095` n `8`; equity avg `3.9949` n `160`; fx avg `-0.0675` n `6`; index avg `0.4374` n `27`; metal avg `-0.0047` n `20`; unknown avg `5.631` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2314`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
