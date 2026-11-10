# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T06:52:25.166407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1018` n `13`; crypto_alt avg `0.2177` n `239`; crypto_major avg `0.1394` n `8`; equity avg `0.0528` n `160`; fx avg `-0.0197` n `6`; index avg `0.003` n `27`; metal avg `-0.042` n `20`; unknown avg `0.7161` n `1261`
- 1h: commodity avg `-0.2134` n `13`; crypto_alt avg `-0.0528` n `239`; crypto_major avg `-0.3706` n `8`; equity avg `-0.321` n `160`; fx avg `-0.0198` n `6`; index avg `-0.0397` n `27`; metal avg `-0.0952` n `20`; unknown avg `1.1757` n `1235`
- 4h: commodity avg `-0.1205` n `13`; crypto_alt avg `0.6317` n `239`; crypto_major avg `0.0151` n `8`; equity avg `-0.1307` n `160`; fx avg `-0.109` n `6`; index avg `0.0177` n `27`; metal avg `-0.0127` n `20`; unknown avg `1.7852` n `1213`
- 24h: commodity avg `-0.46` n `13`; crypto_alt avg `1.9991` n `239`; crypto_major avg `0.6066` n `8`; equity avg `4.6204` n `160`; fx avg `0.005` n `6`; index avg `0.5199` n `27`; metal avg `0.1962` n `20`; unknown avg `192.4578` n `1063`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
