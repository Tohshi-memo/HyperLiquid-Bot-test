# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T13:37:25.667969+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1353` n `13`; crypto_alt avg `-0.2396` n `239`; crypto_major avg `-0.4534` n `8`; equity avg `-0.8588` n `160`; fx avg `-0.0089` n `6`; index avg `-0.0831` n `27`; metal avg `-0.0521` n `20`; unknown avg `1.0652` n `1262`
- 1h: commodity avg `-0.1768` n `13`; crypto_alt avg `-0.1387` n `239`; crypto_major avg `-0.2781` n `8`; equity avg `-0.9567` n `160`; fx avg `-0.0226` n `6`; index avg `-0.0833` n `27`; metal avg `-0.0381` n `20`; unknown avg `19.2733` n `1256`
- 4h: commodity avg `-0.027` n `13`; crypto_alt avg `-0.3992` n `239`; crypto_major avg `-0.8085` n `8`; equity avg `-1.8222` n `160`; fx avg `-0.0019` n `6`; index avg `-0.136` n `27`; metal avg `-0.1612` n `20`; unknown avg `2.2988` n `1250`
- 24h: commodity avg `-0.6336` n `13`; crypto_alt avg `-0.6066` n `239`; crypto_major avg `-0.9981` n `8`; equity avg `1.7286` n `160`; fx avg `-0.0299` n `6`; index avg `0.2447` n `27`; metal avg `-0.1928` n `20`; unknown avg `3.7863` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2249`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
