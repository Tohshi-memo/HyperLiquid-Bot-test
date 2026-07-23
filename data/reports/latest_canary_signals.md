# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T22:07:24.471570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `-0.0167` n `230`; crypto_major avg `0.0037` n `8`; equity avg `-0.1011` n `100`; fx avg `0.0` n `6`; index avg `-0.0543` n `25`; metal avg `-0.0548` n `20`; unknown avg `-0.0371` n `772`
- 1h: commodity avg `-0.0272` n `12`; crypto_alt avg `-0.2328` n `230`; crypto_major avg `-0.1414` n `8`; equity avg `-0.3969` n `100`; fx avg `0.0001` n `6`; index avg `-0.0644` n `25`; metal avg `-0.0554` n `20`; unknown avg `-0.3182` n `772`
- 4h: commodity avg `-0.2565` n `12`; crypto_alt avg `0.1162` n `230`; crypto_major avg `0.1551` n `8`; equity avg `0.1246` n `100`; fx avg `-0.0053` n `6`; index avg `0.059` n `25`; metal avg `0.0271` n `20`; unknown avg `0.2426` n `772`
- 24h: commodity avg `0.6894` n `12`; crypto_alt avg `-1.7173` n `230`; crypto_major avg `-2.1159` n `8`; equity avg `-1.2722` n `99`; fx avg `-0.0625` n `6`; index avg `-0.2541` n `25`; metal avg `-0.6994` n `20`; unknown avg `-0.2388` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
