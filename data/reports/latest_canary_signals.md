# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T22:07:28.558923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0182` n `13`; crypto_alt avg `-0.0901` n `237`; crypto_major avg `-0.0612` n `8`; equity avg `0.0349` n `154`; fx avg `0.004` n `6`; index avg `0.0131` n `27`; metal avg `-0.0012` n `20`; unknown avg `3.7651` n `1236`
- 1h: commodity avg `-0.0345` n `13`; crypto_alt avg `0.3353` n `237`; crypto_major avg `0.245` n `8`; equity avg `0.1945` n `154`; fx avg `-0.0027` n `6`; index avg `0.0268` n `27`; metal avg `-0.0017` n `20`; unknown avg `2.2995` n `1234`
- 4h: commodity avg `-0.1412` n `13`; crypto_alt avg `-0.6646` n `237`; crypto_major avg `-0.6931` n `8`; equity avg `-0.3455` n `154`; fx avg `-0.0326` n `6`; index avg `-0.0348` n `27`; metal avg `-0.0628` n `20`; unknown avg `11.7132` n `1134`
- 24h: commodity avg `-0.0224` n `13`; crypto_alt avg `-0.4311` n `237`; crypto_major avg `-0.2767` n `8`; equity avg `0.6714` n `153`; fx avg `-0.0184` n `6`; index avg `-0.1209` n `27`; metal avg `-0.087` n `20`; unknown avg `706.4978` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2157`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1832`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1744`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
