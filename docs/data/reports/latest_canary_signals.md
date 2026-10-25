# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T14:22:29.558273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `13`; crypto_alt avg `-0.1102` n `237`; crypto_major avg `-0.0673` n `8`; equity avg `-0.0106` n `152`; fx avg `0.0012` n `6`; index avg `-0.0053` n `26`; metal avg `0.004` n `20`; unknown avg `1.24` n `1231`
- 1h: commodity avg `-0.0277` n `13`; crypto_alt avg `-0.2539` n `237`; crypto_major avg `-0.1281` n `8`; equity avg `-0.0843` n `152`; fx avg `0.0108` n `6`; index avg `0.0046` n `26`; metal avg `0.0344` n `20`; unknown avg `2.04` n `1231`
- 4h: commodity avg `-0.0564` n `13`; crypto_alt avg `0.0728` n `237`; crypto_major avg `0.0839` n `8`; equity avg `0.2409` n `152`; fx avg `0.0284` n `6`; index avg `0.0437` n `26`; metal avg `0.0708` n `20`; unknown avg `1.586` n `1221`
- 24h: commodity avg `-0.176` n `13`; crypto_alt avg `-0.5519` n `237`; crypto_major avg `0.3806` n `8`; equity avg `0.4707` n `152`; fx avg `0.02` n `6`; index avg `0.1157` n `26`; metal avg `0.0723` n `20`; unknown avg `11.3467` n `1080`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2222`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
