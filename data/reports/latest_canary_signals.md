# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T22:22:24.019582+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `-0.005` n `231`; crypto_major avg `-0.0043` n `8`; equity avg `-0.0415` n `122`; fx avg `0.0149` n `6`; index avg `-0.0025` n `25`; metal avg `0.0447` n `20`; unknown avg `-0.0719` n `793`
- 1h: commodity avg `-0.0458` n `12`; crypto_alt avg `-0.6674` n `231`; crypto_major avg `-0.4238` n `8`; equity avg `-0.1844` n `122`; fx avg `0.0328` n `6`; index avg `-0.046` n `25`; metal avg `-0.0109` n `20`; unknown avg `0.2801` n `793`
- 4h: commodity avg `-0.0948` n `12`; crypto_alt avg `0.3159` n `231`; crypto_major avg `0.5398` n `8`; equity avg `0.0031` n `122`; fx avg `-0.0859` n `6`; index avg `-0.0303` n `25`; metal avg `0.0441` n `20`; unknown avg `1.079` n `793`
- 24h: commodity avg `-0.1821` n `12`; crypto_alt avg `3.8188` n `231`; crypto_major avg `1.6311` n `8`; equity avg `0.6518` n `122`; fx avg `-0.0684` n `6`; index avg `0.0827` n `25`; metal avg `0.1048` n `20`; unknown avg `5.8627` n `776`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
