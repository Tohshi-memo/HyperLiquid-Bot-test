# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T05:22:23.951460+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.0903` n `230`; crypto_major avg `-0.1901` n `8`; equity avg `-0.0768` n `96`; fx avg `0.0064` n `6`; index avg `0.0196` n `25`; metal avg `-0.0042` n `20`; unknown avg `-0.1996` n `768`
- 1h: commodity avg `-0.0216` n `12`; crypto_alt avg `0.1141` n `230`; crypto_major avg `-0.0955` n `8`; equity avg `-0.3877` n `96`; fx avg `-0.0083` n `6`; index avg `-0.054` n `25`; metal avg `-0.0858` n `20`; unknown avg `-0.3559` n `768`
- 4h: commodity avg `-0.1656` n `12`; crypto_alt avg `-0.3455` n `230`; crypto_major avg `-0.8764` n `8`; equity avg `-1.5148` n `94`; fx avg `-0.0019` n `6`; index avg `-0.2595` n `25`; metal avg `-0.2551` n `20`; unknown avg `0.0667` n `768`
- 24h: commodity avg `-0.062` n `12`; crypto_alt avg `-2.1289` n `230`; crypto_major avg `-3.5042` n `8`; equity avg `-6.0437` n `94`; fx avg `-0.1283` n `6`; index avg `-0.8632` n `25`; metal avg `-0.903` n `20`; unknown avg `-0.5162` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
