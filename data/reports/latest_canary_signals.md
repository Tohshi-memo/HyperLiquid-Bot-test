# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T20:22:27.518586+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0388` n `13`; crypto_alt avg `-0.2258` n `239`; crypto_major avg `-0.2983` n `8`; equity avg `-0.0785` n `158`; fx avg `-0.0001` n `6`; index avg `-0.0194` n `27`; metal avg `-0.0172` n `20`; unknown avg `2.1071` n `1257`
- 1h: commodity avg `-0.0044` n `13`; crypto_alt avg `0.016` n `239`; crypto_major avg `-0.0465` n `8`; equity avg `0.3359` n `158`; fx avg `-0.0007` n `6`; index avg `0.021` n `27`; metal avg `-0.0257` n `20`; unknown avg `5.4294` n `1235`
- 4h: commodity avg `0.1992` n `13`; crypto_alt avg `0.0355` n `239`; crypto_major avg `0.0537` n `8`; equity avg `0.6901` n `158`; fx avg `-0.0073` n `6`; index avg `0.007` n `27`; metal avg `-0.0245` n `20`; unknown avg `77.5992` n `1237`
- 24h: commodity avg `0.1946` n `13`; crypto_alt avg `0.9077` n `239`; crypto_major avg `-0.6629` n `8`; equity avg `1.8825` n `158`; fx avg `-0.1017` n `6`; index avg `0.2108` n `27`; metal avg `-0.1789` n `20`; unknown avg `60.3103` n `1082`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
