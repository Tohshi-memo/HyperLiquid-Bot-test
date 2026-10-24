# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T18:22:29.599309+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `13`; crypto_alt avg `0.1685` n `237`; crypto_major avg `0.092` n `8`; equity avg `0.0036` n `152`; fx avg `-0.0031` n `6`; index avg `-0.002` n `26`; metal avg `0.0039` n `20`; unknown avg `1.8302` n `1231`
- 1h: commodity avg `0.0816` n `13`; crypto_alt avg `0.1092` n `237`; crypto_major avg `0.1744` n `8`; equity avg `-0.043` n `152`; fx avg `-0.001` n `6`; index avg `-0.0081` n `26`; metal avg `0.0037` n `20`; unknown avg `0.8387` n `1231`
- 4h: commodity avg `0.0725` n `13`; crypto_alt avg `-0.1094` n `237`; crypto_major avg `-0.0892` n `8`; equity avg `0.0165` n `152`; fx avg `-0.0177` n `6`; index avg `0.0027` n `26`; metal avg `-0.044` n `20`; unknown avg `0.4278` n `1198`
- 24h: commodity avg `0.2601` n `13`; crypto_alt avg `-3.9581` n `237`; crypto_major avg `-2.5824` n `8`; equity avg `-0.8308` n `152`; fx avg `-0.0341` n `6`; index avg `-0.0973` n `26`; metal avg `-0.2231` n `20`; unknown avg `-0.5203` n `1046`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
