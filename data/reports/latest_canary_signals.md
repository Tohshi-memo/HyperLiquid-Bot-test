# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T14:52:27.740888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0636` n `13`; crypto_alt avg `0.117` n `239`; crypto_major avg `0.1024` n `8`; equity avg `-0.0287` n `158`; fx avg `0.0011` n `6`; index avg `0.0116` n `27`; metal avg `0.0017` n `20`; unknown avg `-0.1811` n `1260`
- 1h: commodity avg `0.0178` n `13`; crypto_alt avg `0.2545` n `239`; crypto_major avg `0.2165` n `8`; equity avg `-0.0116` n `158`; fx avg `0.009` n `6`; index avg `0.0047` n `27`; metal avg `-0.0003` n `20`; unknown avg `0.8125` n `1248`
- 4h: commodity avg `0.0679` n `13`; crypto_alt avg `-0.2588` n `239`; crypto_major avg `0.3281` n `8`; equity avg `0.0515` n `158`; fx avg `-0.0068` n `6`; index avg `-0.0093` n `27`; metal avg `-0.0092` n `20`; unknown avg `0.8441` n `1242`
- 24h: commodity avg `0.1137` n `13`; crypto_alt avg `-1.6695` n `239`; crypto_major avg `-0.1683` n `8`; equity avg `0.1743` n `158`; fx avg `0.0353` n `6`; index avg `0.0091` n `27`; metal avg `-0.0447` n `20`; unknown avg `7.658` n `1091`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
