# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T00:22:28.872473+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0487` n `13`; crypto_alt avg `-0.0176` n `237`; crypto_major avg `0.0008` n `8`; equity avg `0.0837` n `154`; fx avg `-0.0179` n `6`; index avg `0.0087` n `27`; metal avg `0.0017` n `20`; unknown avg `1.5242` n `1238`
- 1h: commodity avg `-0.0657` n `13`; crypto_alt avg `0.6165` n `237`; crypto_major avg `0.6158` n `8`; equity avg `0.7077` n `154`; fx avg `-0.0125` n `6`; index avg `0.1499` n `27`; metal avg `0.0372` n `20`; unknown avg `2.0123` n `1230`
- 4h: commodity avg `-0.1023` n `13`; crypto_alt avg `0.5984` n `237`; crypto_major avg `0.5931` n `8`; equity avg `0.8279` n `154`; fx avg `-0.0324` n `6`; index avg `0.1771` n `27`; metal avg `0.0295` n `20`; unknown avg `10.7255` n `1196`
- 24h: commodity avg `-0.0584` n `13`; crypto_alt avg `0.2305` n `237`; crypto_major avg `0.5625` n `8`; equity avg `1.4394` n `153`; fx avg `-0.06` n `6`; index avg `0.056` n `27`; metal avg `0.0234` n `20`; unknown avg `759.7928` n `972`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2249`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.19`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
