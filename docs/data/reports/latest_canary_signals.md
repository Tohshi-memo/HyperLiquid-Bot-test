# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T17:22:20.451224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0248` n `12`; crypto_alt avg `0.1072` n `228`; crypto_major avg `0.1034` n `8`; equity avg `0.053` n `69`; fx avg `0.0259` n `6`; index avg `0.0222` n `23`; metal avg `0.0062` n `18`; unknown avg `-0.1045` n `421`
- 1h: commodity avg `0.2559` n `12`; crypto_alt avg `0.2161` n `228`; crypto_major avg `0.2737` n `8`; equity avg `0.0081` n `69`; fx avg `-0.0079` n `6`; index avg `0.0512` n `23`; metal avg `0.011` n `18`; unknown avg `-0.0718` n `421`
- 4h: commodity avg `-0.3161` n `12`; crypto_alt avg `0.1835` n `228`; crypto_major avg `0.7271` n `8`; equity avg `-0.0465` n `69`; fx avg `0.0031` n `6`; index avg `-0.0346` n `23`; metal avg `0.0404` n `18`; unknown avg `1.0539` n `421`
- 24h: commodity avg `-0.0466` n `12`; crypto_alt avg `0.4766` n `228`; crypto_major avg `1.3943` n `8`; equity avg `0.7485` n `69`; fx avg `0.0035` n `6`; index avg `0.0206` n `23`; metal avg `-0.0375` n `18`; unknown avg `1.0717` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1908`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
