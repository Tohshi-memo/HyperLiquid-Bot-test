# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T13:22:27.401083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0165` n `12`; crypto_alt avg `-0.4878` n `230`; crypto_major avg `-0.3289` n `8`; equity avg `-0.1768` n `121`; fx avg `-0.0003` n `6`; index avg `-0.0475` n `25`; metal avg `0.0276` n `20`; unknown avg `1.1364` n `793`
- 1h: commodity avg `-0.034` n `12`; crypto_alt avg `0.2241` n `230`; crypto_major avg `0.6431` n `8`; equity avg `-0.0415` n `121`; fx avg `-0.0246` n `6`; index avg `-0.0325` n `25`; metal avg `0.0401` n `20`; unknown avg `1.1774` n `793`
- 4h: commodity avg `0.1292` n `12`; crypto_alt avg `2.258` n `230`; crypto_major avg `0.4174` n `8`; equity avg `0.0153` n `121`; fx avg `-0.0044` n `6`; index avg `0.0022` n `25`; metal avg `-0.0407` n `20`; unknown avg `1.4914` n `793`
- 24h: commodity avg `0.1517` n `12`; crypto_alt avg `7.6163` n `230`; crypto_major avg `5.8556` n `8`; equity avg `1.3401` n `121`; fx avg `-0.0713` n `6`; index avg `0.1673` n `25`; metal avg `0.9445` n `20`; unknown avg `3.4363` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2364`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1924`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
