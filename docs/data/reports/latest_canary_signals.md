# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T04:52:25.124629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0338` n `12`; crypto_alt avg `0.0721` n `228`; crypto_major avg `0.0574` n `8`; equity avg `0.1332` n `74`; fx avg `0.0102` n `6`; index avg `0.0186` n `23`; metal avg `-0.0858` n `18`; unknown avg `-0.4863` n `547`
- 1h: commodity avg `-0.0283` n `12`; crypto_alt avg `-0.4907` n `228`; crypto_major avg `-0.5317` n `8`; equity avg `-0.5066` n `74`; fx avg `0.0054` n `6`; index avg `-0.3853` n `23`; metal avg `-0.5071` n `18`; unknown avg `-0.9188` n `547`
- 4h: commodity avg `-0.2927` n `12`; crypto_alt avg `-0.9548` n `228`; crypto_major avg `-0.9947` n `8`; equity avg `-1.0335` n `74`; fx avg `0.0941` n `6`; index avg `-0.5435` n `23`; metal avg `-1.0579` n `18`; unknown avg `-0.8768` n `547`
- 24h: commodity avg `-0.594` n `12`; crypto_alt avg `-1.703` n `228`; crypto_major avg `-3.9454` n `8`; equity avg `-3.9076` n `74`; fx avg `0.1396` n `6`; index avg `-1.8225` n `23`; metal avg `-3.2573` n `18`; unknown avg `0.4834` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0514`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.043`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0427`, n `668`, weak_sample_signal
