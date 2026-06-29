# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-29T02:37:29.177723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0662` n `12`; crypto_alt avg `0.4542` n `228`; crypto_major avg `0.4701` n `8`; equity avg `0.0228` n `88`; fx avg `0.0111` n `6`; index avg `0.0036` n `23`; metal avg `-0.0628` n `20`; unknown avg `0.0833` n `764`
- 1h: commodity avg `-0.0832` n `12`; crypto_alt avg `0.2896` n `228`; crypto_major avg `0.3398` n `8`; equity avg `-0.1113` n `88`; fx avg `0.0399` n `6`; index avg `-0.0353` n `23`; metal avg `0.0407` n `20`; unknown avg `-0.0907` n `764`
- 4h: commodity avg `-0.0922` n `12`; crypto_alt avg `0.786` n `228`; crypto_major avg `0.8532` n `8`; equity avg `-0.6424` n `88`; fx avg `0.1041` n `6`; index avg `-0.2444` n `23`; metal avg `-0.0257` n `20`; unknown avg `1.6585` n `762`
- 24h: commodity avg `-0.5402` n `12`; crypto_alt avg `-0.084` n `228`; crypto_major avg `-0.2465` n `8`; equity avg `-0.1864` n `88`; fx avg `0.0397` n `6`; index avg `-0.0632` n `23`; metal avg `-0.2165` n `20`; unknown avg `-0.8812` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1962`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.183`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
