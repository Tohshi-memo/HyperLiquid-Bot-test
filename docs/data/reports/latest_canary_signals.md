# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T09:07:31.735647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1126` n `13`; crypto_alt avg `-0.2235` n `239`; crypto_major avg `-0.3066` n `8`; equity avg `-0.3038` n `160`; fx avg `0.0025` n `6`; index avg `-0.0512` n `27`; metal avg `-0.1155` n `20`; unknown avg `-0.0082` n `1246`
- 1h: commodity avg `-0.1277` n `13`; crypto_alt avg `-0.2002` n `239`; crypto_major avg `-0.4789` n `8`; equity avg `-0.2512` n `160`; fx avg `0.0244` n `6`; index avg `-0.0386` n `27`; metal avg `-0.081` n `20`; unknown avg `0.0178` n `1235`
- 4h: commodity avg `-0.2352` n `13`; crypto_alt avg `-0.1796` n `239`; crypto_major avg `-0.6809` n `8`; equity avg `0.1146` n `160`; fx avg `-0.0576` n `6`; index avg `0.0343` n `27`; metal avg `-0.1759` n `20`; unknown avg `1.5816` n `1199`
- 24h: commodity avg `-0.6855` n `13`; crypto_alt avg `1.0485` n `239`; crypto_major avg `-0.4484` n `8`; equity avg `4.4364` n `160`; fx avg `-0.0492` n `6`; index avg `0.4653` n `27`; metal avg `0.0739` n `20`; unknown avg `5.8349` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
