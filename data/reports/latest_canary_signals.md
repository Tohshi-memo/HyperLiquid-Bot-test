# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T04:22:20.331827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1616` n `12`; crypto_alt avg `0.0901` n `228`; crypto_major avg `-0.0678` n `8`; equity avg `0.0733` n `69`; fx avg `-0.0072` n `6`; index avg `0.041` n `23`; metal avg `0.0887` n `18`; unknown avg `-0.2571` n `417`
- 1h: commodity avg `0.0046` n `12`; crypto_alt avg `-0.3116` n `228`; crypto_major avg `-0.3168` n `8`; equity avg `0.0925` n `69`; fx avg `-0.0083` n `6`; index avg `0.0743` n `23`; metal avg `0.1192` n `18`; unknown avg `-0.5246` n `417`
- 4h: commodity avg `-0.1761` n `12`; crypto_alt avg `-0.7793` n `228`; crypto_major avg `-0.8384` n `8`; equity avg `0.0165` n `69`; fx avg `0.0054` n `6`; index avg `-0.015` n `23`; metal avg `-0.0821` n `18`; unknown avg `-0.4717` n `417`
- 24h: commodity avg `-0.4079` n `12`; crypto_alt avg `1.0047` n `228`; crypto_major avg `1.8269` n `8`; equity avg `4.8216` n `69`; fx avg `0.1371` n `6`; index avg `1.762` n `23`; metal avg `2.4699` n `18`; unknown avg `0.5837` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
