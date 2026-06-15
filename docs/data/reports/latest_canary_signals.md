# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T08:22:39.368211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.67` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1072` n `12`; crypto_alt avg `-0.1563` n `228`; crypto_major avg `-0.1016` n `8`; equity avg `0.0427` n `74`; fx avg `-0.0189` n `6`; index avg `0.0269` n `23`; metal avg `0.0375` n `18`; unknown avg `-0.0173` n `689`
- 1h: commodity avg `0.1917` n `12`; crypto_alt avg `-0.2491` n `228`; crypto_major avg `-0.1987` n `8`; equity avg `0.0273` n `74`; fx avg `-0.0033` n `6`; index avg `0.0295` n `23`; metal avg `0.1891` n `18`; unknown avg `0.96` n `689`
- 4h: commodity avg `-0.0774` n `12`; crypto_alt avg `-0.1267` n `228`; crypto_major avg `-0.1942` n `8`; equity avg `0.112` n `74`; fx avg `0.0055` n `6`; index avg `0.139` n `23`; metal avg `0.0738` n `18`; unknown avg `0.8156` n `529`
- 24h: commodity avg `-0.7563` n `12`; crypto_alt avg `2.7437` n `228`; crypto_major avg `2.8749` n `8`; equity avg `1.7245` n `74`; fx avg `0.0371` n `6`; index avg `0.9675` n `23`; metal avg `2.0024` n `18`; unknown avg `1.6653` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
