# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T06:52:29.337828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0606` n `12`; crypto_alt avg `-0.1915` n `228`; crypto_major avg `-0.1444` n `8`; equity avg `0.0535` n `79`; fx avg `-0.0328` n `6`; index avg `0.0144` n `23`; metal avg `0.1042` n `18`; unknown avg `-0.0014` n `701`
- 1h: commodity avg `0.0712` n `12`; crypto_alt avg `-0.1102` n `228`; crypto_major avg `-0.172` n `8`; equity avg `0.2672` n `79`; fx avg `-0.0034` n `6`; index avg `0.0488` n `23`; metal avg `0.1894` n `18`; unknown avg `0.138` n `669`
- 4h: commodity avg `0.0183` n `12`; crypto_alt avg `-0.4163` n `228`; crypto_major avg `-0.658` n `8`; equity avg `0.3033` n `79`; fx avg `-0.0333` n `6`; index avg `0.0373` n `23`; metal avg `0.4618` n `18`; unknown avg `-0.1738` n `669`
- 24h: commodity avg `-0.2662` n `12`; crypto_alt avg `-0.1039` n `228`; crypto_major avg `-0.7576` n `8`; equity avg `-0.3918` n `79`; fx avg `-0.0045` n `6`; index avg `0.0101` n `23`; metal avg `0.5731` n `18`; unknown avg `-0.3321` n `643`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
