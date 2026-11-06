# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T22:07:27.589690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0202` n `13`; crypto_alt avg `0.0679` n `239`; crypto_major avg `0.2739` n `8`; equity avg `0.0328` n `158`; fx avg `-0.005` n `6`; index avg `0.0136` n `27`; metal avg `0.0158` n `20`; unknown avg `2.0332` n `1249`
- 1h: commodity avg `0.0646` n `13`; crypto_alt avg `0.0313` n `239`; crypto_major avg `0.3099` n `8`; equity avg `0.1021` n `158`; fx avg `-0.0057` n `6`; index avg `-0.0084` n `27`; metal avg `0.0217` n `20`; unknown avg `1.5566` n `1215`
- 4h: commodity avg `0.2438` n `13`; crypto_alt avg `0.0041` n `239`; crypto_major avg `0.2332` n `8`; equity avg `1.0025` n `158`; fx avg `0.0241` n `6`; index avg `0.0455` n `27`; metal avg `0.0508` n `20`; unknown avg `1.084` n `1183`
- 24h: commodity avg `0.0181` n `13`; crypto_alt avg `1.9309` n `239`; crypto_major avg `0.2471` n `8`; equity avg `3.0398` n `158`; fx avg `-0.0921` n `6`; index avg `0.4433` n `27`; metal avg `0.0566` n `20`; unknown avg `1.1541` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
