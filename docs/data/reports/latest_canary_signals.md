# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T06:37:33.556064+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0317` n `13`; crypto_alt avg `-0.275` n `237`; crypto_major avg `-0.1518` n `8`; equity avg `-0.0698` n `152`; fx avg `-0.0236` n `6`; index avg `-0.0323` n `26`; metal avg `-0.018` n `20`; unknown avg `0.0109` n `1240`
- 1h: commodity avg `0.0169` n `13`; crypto_alt avg `-0.5337` n `237`; crypto_major avg `-0.2519` n `8`; equity avg `-0.3667` n `152`; fx avg `0.0017` n `6`; index avg `-0.0984` n `26`; metal avg `-0.1053` n `20`; unknown avg `0.6799` n `1212`
- 4h: commodity avg `0.0285` n `13`; crypto_alt avg `0.1967` n `237`; crypto_major avg `0.3989` n `8`; equity avg `0.2446` n `152`; fx avg `0.0258` n `6`; index avg `-0.0128` n `26`; metal avg `0.0534` n `20`; unknown avg `2.5444` n `1198`
- 24h: commodity avg `-0.5909` n `13`; crypto_alt avg `-0.8706` n `237`; crypto_major avg `-0.6086` n `8`; equity avg `-0.5585` n `152`; fx avg `0.0479` n `6`; index avg `-0.059` n `26`; metal avg `0.1168` n `20`; unknown avg `0.5679` n `985`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2554`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1965`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
