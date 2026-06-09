# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T22:37:31.409690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1337` n `12`; crypto_alt avg `-0.1501` n `228`; crypto_major avg `-0.1822` n `8`; equity avg `-0.2252` n `74`; fx avg `0.0033` n `6`; index avg `-0.0909` n `23`; metal avg `-0.0883` n `18`; unknown avg `-0.0796` n `547`
- 1h: commodity avg `0.0495` n `12`; crypto_alt avg `-0.1458` n `228`; crypto_major avg `-0.264` n `8`; equity avg `-0.172` n `74`; fx avg `0.0746` n `6`; index avg `0.0497` n `23`; metal avg `-0.1349` n `18`; unknown avg `-0.0841` n `547`
- 4h: commodity avg `0.1673` n `12`; crypto_alt avg `-0.1653` n `228`; crypto_major avg `-0.3979` n `8`; equity avg `-0.269` n `74`; fx avg `-0.0257` n `6`; index avg `0.4696` n `23`; metal avg `-0.3249` n `18`; unknown avg `0.0053` n `547`
- 24h: commodity avg `-0.5683` n `12`; crypto_alt avg `-1.6904` n `228`; crypto_major avg `-3.0206` n `8`; equity avg `-2.115` n `74`; fx avg `0.0723` n `6`; index avg `-0.8795` n `23`; metal avg `-1.5511` n `18`; unknown avg `-0.5621` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0411`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0383`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0369`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0366`, n `668`, weak_sample_signal
