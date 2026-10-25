# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T15:07:29.008120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `13`; crypto_alt avg `0.2766` n `237`; crypto_major avg `0.1958` n `8`; equity avg `0.0323` n `152`; fx avg `-0.0028` n `6`; index avg `0.0058` n `26`; metal avg `-0.0008` n `20`; unknown avg `-0.0841` n `1230`
- 1h: commodity avg `-0.0068` n `13`; crypto_alt avg `0.6045` n `237`; crypto_major avg `0.4955` n `8`; equity avg `0.1534` n `152`; fx avg `-0.0059` n `6`; index avg `0.0127` n `26`; metal avg `0.0093` n `20`; unknown avg `2.6894` n `1231`
- 4h: commodity avg `-0.1042` n `13`; crypto_alt avg `0.9907` n `237`; crypto_major avg `0.6889` n `8`; equity avg `0.4023` n `152`; fx avg `0.0014` n `6`; index avg `0.0687` n `26`; metal avg `0.0706` n `20`; unknown avg `0.0866` n `1225`
- 24h: commodity avg `-0.1792` n `13`; crypto_alt avg `0.6925` n `237`; crypto_major avg `1.6955` n `8`; equity avg `0.6971` n `152`; fx avg `0.0105` n `6`; index avg `0.1377` n `26`; metal avg `0.1094` n `20`; unknown avg `18.6265` n `1080`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2237`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
