# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T20:37:31.926252+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `0.0341` n `232`; crypto_major avg `0.067` n `8`; equity avg `0.0243` n `133`; fx avg `-0.0068` n `6`; index avg `0.0027` n `26`; metal avg `0.0084` n `20`; unknown avg `13.3269` n `782`
- 1h: commodity avg `0.0703` n `12`; crypto_alt avg `-0.2205` n `232`; crypto_major avg `-0.1411` n `8`; equity avg `-0.0338` n `133`; fx avg `-0.0032` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0215` n `20`; unknown avg `13.2885` n `778`
- 4h: commodity avg `0.0357` n `12`; crypto_alt avg `0.4774` n `232`; crypto_major avg `0.5871` n `8`; equity avg `0.2192` n `133`; fx avg `0.0178` n `6`; index avg `0.0327` n `26`; metal avg `-0.06` n `20`; unknown avg `2.1036` n `778`
- 24h: commodity avg `-0.0898` n `12`; crypto_alt avg `4.2231` n `232`; crypto_major avg `5.3285` n `8`; equity avg `1.5218` n `133`; fx avg `-0.2304` n `6`; index avg `0.2055` n `26`; metal avg `0.7632` n `20`; unknown avg `1.0186` n `736`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
