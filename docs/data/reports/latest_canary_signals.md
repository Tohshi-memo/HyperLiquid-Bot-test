# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T04:37:12.594910+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0221` n `12`; crypto_alt avg `0.082` n `228`; crypto_major avg `-0.0258` n `8`; equity avg `-0.0022` n `67`; fx avg `0.0` n `6`; index avg `0.0096` n `23`; metal avg `0.0051` n `18`; unknown avg `0.1935` n `386`
- 1h: commodity avg `0.0613` n `12`; crypto_alt avg `-0.4951` n `228`; crypto_major avg `-0.1588` n `8`; equity avg `-0.0043` n `67`; fx avg `-0.0012` n `6`; index avg `0.0081` n `23`; metal avg `0.0139` n `18`; unknown avg `-0.0828` n `386`
- 4h: commodity avg `0.1416` n `12`; crypto_alt avg `0.8616` n `228`; crypto_major avg `0.4876` n `8`; equity avg `0.2471` n `67`; fx avg `-0.0045` n `6`; index avg `0.1371` n `23`; metal avg `0.0492` n `18`; unknown avg `-0.6775` n `386`
- 24h: commodity avg `0.2529` n `12`; crypto_alt avg `-3.8909` n `228`; crypto_major avg `-2.6101` n `8`; equity avg `-1.8847` n `67`; fx avg `0.0524` n `6`; index avg `-0.0537` n `23`; metal avg `-0.9264` n `18`; unknown avg `-2.0066` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0477`, n `668`, weak_sample_signal
