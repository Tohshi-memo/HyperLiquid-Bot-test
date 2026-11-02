# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T16:52:35.454335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0607` n `13`; crypto_alt avg `-0.1172` n `239`; crypto_major avg `-0.079` n `8`; equity avg `-0.0958` n `156`; fx avg `-0.0022` n `6`; index avg `0.0012` n `27`; metal avg `-0.0047` n `20`; unknown avg `0.0421` n `1265`
- 1h: commodity avg `-0.2539` n `13`; crypto_alt avg `-0.3236` n `239`; crypto_major avg `-0.2133` n `8`; equity avg `-0.6053` n `156`; fx avg `0.0003` n `6`; index avg `-0.0391` n `27`; metal avg `0.0348` n `20`; unknown avg `-0.0885` n `1253`
- 4h: commodity avg `-0.7616` n `13`; crypto_alt avg `-0.2463` n `238`; crypto_major avg `-0.216` n `8`; equity avg `-1.2964` n `156`; fx avg `0.0026` n `6`; index avg `0.0088` n `27`; metal avg `0.4493` n `20`; unknown avg `219.2233` n `1253`
- 24h: commodity avg `-1.1503` n `13`; crypto_alt avg `-2.2165` n `238`; crypto_major avg `-0.9045` n `8`; equity avg `-0.8955` n `156`; fx avg `0.2628` n `6`; index avg `0.2107` n `27`; metal avg `0.4164` n `20`; unknown avg `7.3362` n `1077`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1707`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1567`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
