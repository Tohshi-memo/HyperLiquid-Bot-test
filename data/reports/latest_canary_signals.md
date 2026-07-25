# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T15:52:27.446443+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0236` n `12`; crypto_alt avg `0.0549` n `230`; crypto_major avg `0.0205` n `8`; equity avg `0.0115` n `100`; fx avg `-0.0024` n `6`; index avg `-0.0054` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.0033` n `774`
- 1h: commodity avg `-0.0269` n `12`; crypto_alt avg `0.326` n `230`; crypto_major avg `0.3348` n `8`; equity avg `0.008` n `100`; fx avg `-0.0011` n `6`; index avg `0.0033` n `25`; metal avg `-0.0075` n `20`; unknown avg `0.2787` n `774`
- 4h: commodity avg `-0.3634` n `12`; crypto_alt avg `0.6275` n `230`; crypto_major avg `0.6225` n `8`; equity avg `0.0537` n `100`; fx avg `-0.0002` n `6`; index avg `0.0085` n `25`; metal avg `0.0194` n `20`; unknown avg `0.0152` n `774`
- 24h: commodity avg `-0.3834` n `12`; crypto_alt avg `0.1137` n `230`; crypto_major avg `0.4682` n `8`; equity avg `-1.1516` n `100`; fx avg `-0.0439` n `6`; index avg `-0.1779` n `25`; metal avg `-0.2126` n `20`; unknown avg `-0.3152` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1647`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1246`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.115`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1087`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
