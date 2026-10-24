# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T19:07:30.561175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `13`; crypto_alt avg `0.0143` n `237`; crypto_major avg `0.1137` n `8`; equity avg `0.0973` n `152`; fx avg `-0.0122` n `6`; index avg `0.0295` n `26`; metal avg `0.0185` n `20`; unknown avg `5.1136` n `1229`
- 1h: commodity avg `-0.0929` n `13`; crypto_alt avg `0.6007` n `237`; crypto_major avg `0.5305` n `8`; equity avg `0.2837` n `152`; fx avg `-0.0126` n `6`; index avg `0.0413` n `26`; metal avg `0.0253` n `20`; unknown avg `5.3163` n `1231`
- 4h: commodity avg `-0.0306` n `13`; crypto_alt avg `0.8648` n `237`; crypto_major avg `1.0927` n `8`; equity avg `0.3565` n `152`; fx avg `-0.0296` n `6`; index avg `0.05` n `26`; metal avg `0.009` n `20`; unknown avg `1.9519` n `1200`
- 24h: commodity avg `0.1284` n `13`; crypto_alt avg `-2.9086` n `237`; crypto_major avg `-1.8238` n `8`; equity avg `-0.2764` n `152`; fx avg `-0.0463` n `6`; index avg `-0.0186` n `26`; metal avg `-0.1775` n `20`; unknown avg `-0.5763` n `1046`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1914`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1823`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
