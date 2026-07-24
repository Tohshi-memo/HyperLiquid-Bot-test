# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T00:22:27.822202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `12`; crypto_alt avg `0.0904` n `230`; crypto_major avg `0.0455` n `8`; equity avg `-0.0245` n `100`; fx avg `0.005` n `6`; index avg `-0.0373` n `25`; metal avg `0.0051` n `20`; unknown avg `0.0475` n `772`
- 1h: commodity avg `0.047` n `12`; crypto_alt avg `-0.255` n `230`; crypto_major avg `-0.4139` n `8`; equity avg `-0.3424` n `100`; fx avg `-0.0228` n `6`; index avg `-0.0946` n `25`; metal avg `-0.0239` n `20`; unknown avg `-0.2069` n `772`
- 4h: commodity avg `0.099` n `12`; crypto_alt avg `-0.6393` n `230`; crypto_major avg `-0.5367` n `8`; equity avg `-0.7129` n `100`; fx avg `-0.0281` n `6`; index avg `-0.1501` n `25`; metal avg `-0.0412` n `20`; unknown avg `-0.2334` n `772`
- 24h: commodity avg `0.7011` n `12`; crypto_alt avg `-1.9687` n `230`; crypto_major avg `-2.6992` n `8`; equity avg `-1.8916` n `99`; fx avg `-0.092` n `6`; index avg `-0.4432` n `25`; metal avg `-0.7928` n `20`; unknown avg `-0.2885` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
