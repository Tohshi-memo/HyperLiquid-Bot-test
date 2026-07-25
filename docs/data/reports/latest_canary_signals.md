# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T13:58:06.869081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.37` n `12`; crypto_alt avg `-0.0312` n `230`; crypto_major avg `-0.0168` n `8`; equity avg `-0.0217` n `100`; fx avg `-0.0037` n `6`; index avg `0.0106` n `25`; metal avg `0.0175` n `20`; unknown avg `0.0835` n `774`
- 1h: commodity avg `-0.3852` n `12`; crypto_alt avg `0.116` n `230`; crypto_major avg `0.1463` n `8`; equity avg `-0.0524` n `100`; fx avg `0.0017` n `6`; index avg `0.0125` n `25`; metal avg `0.0155` n `20`; unknown avg `0.0511` n `774`
- 4h: commodity avg `-0.4674` n `12`; crypto_alt avg `0.1376` n `230`; crypto_major avg `0.0859` n `8`; equity avg `0.0015` n `100`; fx avg `-0.0057` n `6`; index avg `0.0071` n `25`; metal avg `0.0032` n `20`; unknown avg `-0.0068` n `774`
- 24h: commodity avg `-0.5782` n `12`; crypto_alt avg `0.0099` n `230`; crypto_major avg `0.344` n `8`; equity avg `-0.865` n `100`; fx avg `-0.0125` n `6`; index avg `-0.0094` n `25`; metal avg `-0.0129` n `20`; unknown avg `13.3228` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1243`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1156`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.108`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
