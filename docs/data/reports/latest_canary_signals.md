# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T21:08:05.580765+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `13`; crypto_alt avg `0.3618` n `238`; crypto_major avg `0.2447` n `8`; equity avg `0.4081` n `155`; fx avg `-0.0019` n `6`; index avg `0.0218` n `27`; metal avg `-0.0094` n `20`; unknown avg `1.13` n `1224`
- 1h: commodity avg `0.0838` n `13`; crypto_alt avg `-0.4392` n `238`; crypto_major avg `-0.3647` n `8`; equity avg `-0.9456` n `155`; fx avg `-0.007` n `6`; index avg `-0.1835` n `27`; metal avg `-0.1227` n `20`; unknown avg `4.4314` n `1146`
- 4h: commodity avg `-0.3672` n `13`; crypto_alt avg `1.6873` n `238`; crypto_major avg `1.1089` n `8`; equity avg `-0.0789` n `155`; fx avg `-0.0278` n `6`; index avg `-0.0896` n `27`; metal avg `0.1081` n `20`; unknown avg `8.9917` n `1114`
- 24h: commodity avg `0.1199` n `13`; crypto_alt avg `1.2601` n `238`; crypto_major avg `0.8841` n `8`; equity avg `1.2608` n `154`; fx avg `0.246` n `6`; index avg `0.1908` n `27`; metal avg `-0.1019` n `20`; unknown avg `153.2107` n `1060`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
