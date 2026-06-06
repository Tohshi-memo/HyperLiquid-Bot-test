# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T12:00:48.379299+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0437` n `12`; crypto_alt avg `-0.0881` n `228`; crypto_major avg `-0.1133` n `8`; equity avg `-0.0692` n `74`; fx avg `-0.0005` n `6`; index avg `0.062` n `23`; metal avg `0.0096` n `18`; unknown avg `-0.0515` n `423`
- 1h: commodity avg `-0.0916` n `12`; crypto_alt avg `0.2267` n `228`; crypto_major avg `0.3364` n `8`; equity avg `0.1621` n `74`; fx avg `0.0032` n `6`; index avg `0.0378` n `23`; metal avg `0.0783` n `18`; unknown avg `0.2753` n `421`
- 4h: commodity avg `0.1521` n `12`; crypto_alt avg `-0.0341` n `228`; crypto_major avg `-0.3522` n `8`; equity avg `0.5177` n `74`; fx avg `0.0098` n `6`; index avg `0.3376` n `23`; metal avg `0.0852` n `18`; unknown avg `0.0005` n `421`
- 24h: commodity avg `-1.186` n `12`; crypto_alt avg `-3.3392` n `228`; crypto_major avg `-3.3674` n `8`; equity avg `-6.5127` n `74`; fx avg `-0.2802` n `6`; index avg `-3.9523` n `23`; metal avg `-4.574` n `18`; unknown avg `-0.8267` n `410`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
