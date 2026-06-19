# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T20:52:28.972081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0219` n `12`; crypto_alt avg `0.2786` n `228`; crypto_major avg `0.2352` n `8`; equity avg `0.0442` n `78`; fx avg `0.0494` n `6`; index avg `-0.0066` n `23`; metal avg `0.0547` n `18`; unknown avg `-0.1269` n `687`
- 1h: commodity avg `0.0485` n `12`; crypto_alt avg `0.1839` n `228`; crypto_major avg `0.0485` n `8`; equity avg `0.0366` n `78`; fx avg `-0.0008` n `6`; index avg `-0.0082` n `23`; metal avg `0.1077` n `18`; unknown avg `-0.0786` n `687`
- 4h: commodity avg `-0.0603` n `12`; crypto_alt avg `-0.13` n `228`; crypto_major avg `0.2408` n `8`; equity avg `-0.0295` n `78`; fx avg `0.0215` n `6`; index avg `-0.0529` n `23`; metal avg `0.1784` n `18`; unknown avg `0.0058` n `687`
- 24h: commodity avg `0.3232` n `12`; crypto_alt avg `-3.6336` n `228`; crypto_major avg `-4.5003` n `8`; equity avg `0.7074` n `78`; fx avg `-0.0941` n `6`; index avg `0.2131` n `23`; metal avg `-4.109` n `18`; unknown avg `-0.301` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
