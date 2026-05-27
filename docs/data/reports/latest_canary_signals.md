# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T11:22:20.373790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0454` n `12`; crypto_alt avg `0.124` n `228`; crypto_major avg `-0.0482` n `8`; equity avg `0.0072` n `67`; fx avg `0.006` n `6`; index avg `-0.01` n `23`; metal avg `-0.1146` n `18`; unknown avg `-0.0617` n `418`
- 1h: commodity avg `0.3124` n `12`; crypto_alt avg `0.2793` n `228`; crypto_major avg `0.0259` n `8`; equity avg `0.0964` n `67`; fx avg `0.0097` n `6`; index avg `0.0954` n `23`; metal avg `-0.7096` n `18`; unknown avg `-0.0174` n `418`
- 4h: commodity avg `-0.1863` n `12`; crypto_alt avg `0.2367` n `228`; crypto_major avg `0.2067` n `8`; equity avg `0.6243` n `67`; fx avg `-0.0684` n `6`; index avg `0.2937` n `23`; metal avg `-0.4366` n `18`; unknown avg `-0.4017` n `418`
- 24h: commodity avg `-0.7858` n `12`; crypto_alt avg `-1.945` n `228`; crypto_major avg `-0.8791` n `8`; equity avg `0.7796` n `67`; fx avg `-0.0403` n `6`; index avg `0.7651` n `23`; metal avg `-1.3102` n `18`; unknown avg `0.2535` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1948`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1906`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1653`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
