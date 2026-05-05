# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T06:45:20.871559+00:00`
- Correlation status: `ready`
- Asset price records: `337`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0882` n `7`; crypto_alt avg `-0.0594` n `223`; crypto_major avg `-0.0277` n `7`; equity avg `0.0347` n `47`; fx avg `-0.0024` n `4`; index avg `0.0981` n `6`; metal avg `0.0737` n `7`; unknown avg `-0.0082` n `312`
- 1h: commodity avg `0.107` n `7`; crypto_alt avg `-0.0578` n `223`; crypto_major avg `-0.0972` n `7`; equity avg `0.0317` n `47`; fx avg `0.008` n `4`; index avg `0.1222` n `6`; metal avg `-0.0168` n `7`; unknown avg `-0.0888` n `310`
- 4h: commodity avg `0.2072` n `7`; crypto_alt avg `-0.1222` n `223`; crypto_major avg `0.1583` n `7`; equity avg `0.5951` n `47`; fx avg `-0.0083` n `4`; index avg `0.3362` n `6`; metal avg `0.0465` n `7`; unknown avg `1.3761` n `310`
- 24h: commodity avg `0.8539` n `7`; crypto_alt avg `0.7823` n `223`; crypto_major avg `0.4164` n `7`; equity avg `-0.1491` n `47`; fx avg `-0.0393` n `4`; index avg `-0.1152` n `6`; metal avg `-1.0143` n `7`; unknown avg `0.5546` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2221`, n `333`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2154`, n `333`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1397`, n `333`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1351`, n `333`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1323`, n `333`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1137`, n `333`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.108`, n `333`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1072`, n `333`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1052`, n `329`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1041`, n `329`, weak_sample_signal
