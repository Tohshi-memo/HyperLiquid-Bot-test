# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T18:22:27.925721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.0063` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.9673` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6046` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1312` n `12`; crypto_alt avg `0.3436` n `228`; crypto_major avg `0.2451` n `8`; equity avg `0.2438` n `67`; fx avg `0.0035` n `6`; index avg `0.0559` n `23`; metal avg `0.1388` n `18`; unknown avg `0.0497` n `418`
- 1h: commodity avg `-0.1363` n `12`; crypto_alt avg `-0.0407` n `228`; crypto_major avg `0.0861` n `8`; equity avg `0.1498` n `67`; fx avg `-0.0038` n `6`; index avg `0.0715` n `23`; metal avg `-0.1829` n `18`; unknown avg `0.6968` n `418`
- 4h: commodity avg `-0.33` n `12`; crypto_alt avg `-2.0375` n `228`; crypto_major avg `-1.9435` n `8`; equity avg `0.0628` n `67`; fx avg `0.0169` n `6`; index avg `0.0238` n `23`; metal avg `-0.3389` n `18`; unknown avg `3.1709` n `416`
- 24h: commodity avg `0.9627` n `12`; crypto_alt avg `-2.1167` n `228`; crypto_major avg `-1.4163` n `8`; equity avg `-0.1986` n `67`; fx avg `-0.124` n `6`; index avg `0.2519` n `23`; metal avg `-1.4238` n `18`; unknown avg `0.7701` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1724`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.169`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
