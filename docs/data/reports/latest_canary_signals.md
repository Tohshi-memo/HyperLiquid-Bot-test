# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T11:07:27.810796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0327` n `12`; crypto_alt avg `-0.9096` n `234`; crypto_major avg `-0.7064` n `8`; equity avg `-0.177` n `140`; fx avg `0.0019` n `6`; index avg `-0.0212` n `26`; metal avg `0.0424` n `20`; unknown avg `2.304` n `923`
- 1h: commodity avg `-0.0161` n `12`; crypto_alt avg `-0.8005` n `234`; crypto_major avg `-0.3531` n `8`; equity avg `-0.1022` n `140`; fx avg `-0.0246` n `6`; index avg `0.0089` n `26`; metal avg `0.0399` n `20`; unknown avg `0.6149` n `923`
- 4h: commodity avg `0.067` n `12`; crypto_alt avg `0.1337` n `234`; crypto_major avg `0.3079` n `8`; equity avg `-0.2866` n `140`; fx avg `0.1132` n `6`; index avg `-0.0496` n `26`; metal avg `0.0334` n `20`; unknown avg `1.2333` n `917`
- 24h: commodity avg `-0.0499` n `12`; crypto_alt avg `5.0546` n `234`; crypto_major avg `4.3477` n `8`; equity avg `1.4682` n `140`; fx avg `0.2236` n `6`; index avg `0.178` n `26`; metal avg `0.5818` n `20`; unknown avg `1.8391` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
