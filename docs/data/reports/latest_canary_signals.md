# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T13:52:16.487522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0996` n `12`; crypto_alt avg `0.0242` n `228`; crypto_major avg `-0.069` n `8`; equity avg `-0.0157` n `67`; fx avg `0.0043` n `6`; index avg `-0.0134` n `23`; metal avg `-0.0139` n `18`; unknown avg `0.0452` n `396`
- 1h: commodity avg `0.115` n `12`; crypto_alt avg `-0.1168` n `228`; crypto_major avg `-0.107` n `8`; equity avg `-0.0529` n `67`; fx avg `0.0319` n `6`; index avg `-0.0765` n `23`; metal avg `-0.131` n `18`; unknown avg `0.2056` n `396`
- 4h: commodity avg `0.222` n `12`; crypto_alt avg `-0.791` n `228`; crypto_major avg `-0.3212` n `8`; equity avg `0.0892` n `67`; fx avg `0.0219` n `6`; index avg `-0.1386` n `23`; metal avg `-0.2271` n `18`; unknown avg `0.9559` n `396`
- 24h: commodity avg `-2.4837` n `12`; crypto_alt avg `2.39` n `228`; crypto_major avg `4.0297` n `8`; equity avg `2.553` n `67`; fx avg `0.09` n `6`; index avg `1.0036` n `23`; metal avg `1.0313` n `18`; unknown avg `1.9469` n `386`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
