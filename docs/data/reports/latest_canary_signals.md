# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T12:07:21.535246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `-0.0232` n `228`; crypto_major avg `0.0068` n `8`; equity avg `0.1006` n `74`; fx avg `-0.0011` n `6`; index avg `0.1732` n `23`; metal avg `0.0191` n `18`; unknown avg `-0.0475` n `423`
- 1h: commodity avg `-0.0377` n `12`; crypto_alt avg `0.292` n `228`; crypto_major avg `0.4567` n `8`; equity avg `0.3323` n `74`; fx avg `0.0026` n `6`; index avg `0.1491` n `23`; metal avg `0.0877` n `18`; unknown avg `0.2854` n `421`
- 4h: commodity avg `0.2061` n `12`; crypto_alt avg `0.0316` n `228`; crypto_major avg `-0.2326` n `8`; equity avg `0.6896` n `74`; fx avg `0.0091` n `6`; index avg `0.4496` n `23`; metal avg `0.0947` n `18`; unknown avg `0.0028` n `421`
- 24h: commodity avg `-1.1332` n `12`; crypto_alt avg `-3.2796` n `228`; crypto_major avg `-3.2515` n `8`; equity avg `-6.3577` n `74`; fx avg `-0.2808` n `6`; index avg `-3.8473` n `23`; metal avg `-4.5653` n `18`; unknown avg `-0.8251` n `410`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
