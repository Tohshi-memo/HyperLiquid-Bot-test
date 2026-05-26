# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T22:22:19.510392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0769` n `12`; crypto_alt avg `0.1372` n `228`; crypto_major avg `0.1584` n `8`; equity avg `0.0379` n `67`; fx avg `0.0039` n `6`; index avg `-0.0351` n `23`; metal avg `0.0257` n `18`; unknown avg `-0.0035` n `418`
- 1h: commodity avg `-0.2806` n `12`; crypto_alt avg `-0.139` n `228`; crypto_major avg `-0.031` n `8`; equity avg `0.0092` n `67`; fx avg `0.0101` n `6`; index avg `-0.0365` n `23`; metal avg `0.0592` n `18`; unknown avg `-0.2719` n `418`
- 4h: commodity avg `-0.1513` n `12`; crypto_alt avg `-0.5858` n `228`; crypto_major avg `-0.7761` n `8`; equity avg `-0.1133` n `67`; fx avg `0.0334` n `6`; index avg `-0.0044` n `23`; metal avg `0.6237` n `18`; unknown avg `-0.5033` n `418`
- 24h: commodity avg `0.9112` n `12`; crypto_alt avg `-1.9552` n `228`; crypto_major avg `-1.7885` n `8`; equity avg `-0.317` n `67`; fx avg `-0.1204` n `6`; index avg `0.4166` n `23`; metal avg `-0.8634` n `18`; unknown avg `0.0246` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1759`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
