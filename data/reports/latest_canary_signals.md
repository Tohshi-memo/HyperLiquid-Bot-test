# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T14:22:22.980857+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.7114` n `12`; crypto_alt avg `0.7723` n `228`; crypto_major avg `0.9076` n `8`; equity avg `0.3308` n `67`; fx avg `0.0029` n `6`; index avg `0.2812` n `23`; metal avg `0.7441` n `18`; unknown avg `0.2931` n `419`
- 1h: commodity avg `-0.3417` n `12`; crypto_alt avg `0.0312` n `228`; crypto_major avg `0.5396` n `8`; equity avg `0.5524` n `67`; fx avg `-0.0189` n `6`; index avg `0.293` n `23`; metal avg `0.4475` n `18`; unknown avg `0.081` n `419`
- 4h: commodity avg `0.0474` n `12`; crypto_alt avg `-0.3162` n `228`; crypto_major avg `0.2895` n `8`; equity avg `0.9344` n `67`; fx avg `0.0882` n `6`; index avg `0.4862` n `23`; metal avg `0.7121` n `18`; unknown avg `-0.1963` n `419`
- 24h: commodity avg `0.3057` n `12`; crypto_alt avg `-4.6357` n `228`; crypto_major avg `-2.3577` n `8`; equity avg `-0.001` n `67`; fx avg `-0.0383` n `6`; index avg `0.1305` n `23`; metal avg `-0.5092` n `18`; unknown avg `-1.5166` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1825`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1545`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
