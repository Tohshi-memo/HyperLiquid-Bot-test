# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T21:52:28.241647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `13`; crypto_alt avg `-0.1126` n `236`; crypto_major avg `0.0022` n `8`; equity avg `-0.1551` n `151`; fx avg `0.0024` n `6`; index avg `-0.0185` n `26`; metal avg `-0.0106` n `20`; unknown avg `0.1908` n `1193`
- 1h: commodity avg `0.0586` n `13`; crypto_alt avg `0.025` n `236`; crypto_major avg `0.1583` n `8`; equity avg `-0.2308` n `151`; fx avg `-0.0004` n `6`; index avg `-0.0065` n `26`; metal avg `0.0166` n `20`; unknown avg `3.5985` n `1185`
- 4h: commodity avg `0.1246` n `13`; crypto_alt avg `0.1574` n `236`; crypto_major avg `0.3789` n `8`; equity avg `-0.7694` n `151`; fx avg `0.0095` n `6`; index avg `-0.1259` n `26`; metal avg `0.0203` n `20`; unknown avg `3.2701` n `1109`
- 24h: commodity avg `0.4373` n `13`; crypto_alt avg `-1.6408` n `236`; crypto_major avg `-1.4288` n `8`; equity avg `-4.0257` n `151`; fx avg `0.0272` n `6`; index avg `-0.6619` n `26`; metal avg `-0.0876` n `20`; unknown avg `0.2122` n `896`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1615`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1144`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1102`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0921`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0772`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0722`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0691`, n `666`, weak_sample_signal
