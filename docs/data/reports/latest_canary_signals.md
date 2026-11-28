# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T22:22:33.704038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `13`; crypto_alt avg `0.1316` n `239`; crypto_major avg `0.1219` n `8`; equity avg `-0.0071` n `168`; fx avg `-0.0073` n `6`; index avg `0.0008` n `27`; metal avg `0.0081` n `20`; unknown avg `0.0254` n `1264`
- 1h: commodity avg `0.0945` n `13`; crypto_alt avg `0.2347` n `239`; crypto_major avg `0.1747` n `8`; equity avg `0.0213` n `168`; fx avg `-0.0032` n `6`; index avg `0.0061` n `27`; metal avg `0.0256` n `20`; unknown avg `0.8297` n `1252`
- 4h: commodity avg `0.2629` n `13`; crypto_alt avg `0.0092` n `239`; crypto_major avg `0.1084` n `8`; equity avg `0.199` n `168`; fx avg `-0.0078` n `6`; index avg `0.026` n `27`; metal avg `0.0475` n `20`; unknown avg `1.2507` n `1184`
- 24h: commodity avg `0.0755` n `13`; crypto_alt avg `-3.0954` n `239`; crypto_major avg `-0.7896` n `8`; equity avg `0.099` n `168`; fx avg `-0.0134` n `6`; index avg `-0.0054` n `27`; metal avg `0.0392` n `20`; unknown avg `2.4174` n `1091`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
