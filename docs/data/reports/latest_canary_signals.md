# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T22:52:27.667706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0706` n `12`; crypto_alt avg `-0.2585` n `234`; crypto_major avg `0.0767` n `8`; equity avg `0.0161` n `140`; fx avg `0.0077` n `6`; index avg `-0.0059` n `26`; metal avg `-0.0225` n `20`; unknown avg `4.404` n `943`
- 1h: commodity avg `-0.3409` n `12`; crypto_alt avg `0.2072` n `234`; crypto_major avg `0.6811` n `8`; equity avg `0.31` n `140`; fx avg `0.0945` n `6`; index avg `0.0643` n `26`; metal avg `0.0737` n `20`; unknown avg `2.6448` n `913`
- 4h: commodity avg `-0.342` n `12`; crypto_alt avg `1.0451` n `234`; crypto_major avg `0.7042` n `8`; equity avg `0.4114` n `140`; fx avg `0.0495` n `6`; index avg `0.0744` n `26`; metal avg `0.0635` n `20`; unknown avg `2.0001` n `853`
- 24h: commodity avg `-0.0189` n `12`; crypto_alt avg `1.1022` n `234`; crypto_major avg `0.4719` n `8`; equity avg `0.2357` n `140`; fx avg `0.0456` n `6`; index avg `0.0258` n `26`; metal avg `0.0177` n `20`; unknown avg `3.9325` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
