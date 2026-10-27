# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T09:22:57.045638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0431` n `13`; crypto_alt avg `-0.087` n `238`; crypto_major avg `-0.082` n `8`; equity avg `0.0659` n `154`; fx avg `-0.0156` n `6`; index avg `0.0362` n `27`; metal avg `-0.0277` n `20`; unknown avg `0.2631` n `1238`
- 1h: commodity avg `-0.0698` n `13`; crypto_alt avg `-0.2006` n `238`; crypto_major avg `-0.1603` n `8`; equity avg `0.2006` n `154`; fx avg `-0.0438` n `6`; index avg `0.0701` n `27`; metal avg `0.0319` n `20`; unknown avg `193.65` n `1234`
- 4h: commodity avg `0.2903` n `13`; crypto_alt avg `0.1839` n `237`; crypto_major avg `-0.0122` n `8`; equity avg `0.0571` n `154`; fx avg `-0.0183` n `6`; index avg `0.0204` n `27`; metal avg `-0.1215` n `20`; unknown avg `0.3651` n `1172`
- 24h: commodity avg `0.2535` n `13`; crypto_alt avg `-0.3587` n `237`; crypto_major avg `-0.144` n `8`; equity avg `0.7449` n `153`; fx avg `-0.0651` n `6`; index avg `0.3116` n `27`; metal avg `-0.3397` n `20`; unknown avg `1048.3723` n `1038`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2033`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
