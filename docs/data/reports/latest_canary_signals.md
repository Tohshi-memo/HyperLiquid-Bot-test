# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T10:07:38.445017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.39` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `0.1632` n `228`; crypto_major avg `0.2259` n `8`; equity avg `0.0177` n `74`; fx avg `0.0043` n `6`; index avg `0.0267` n `23`; metal avg `-0.0747` n `18`; unknown avg `-0.0115` n `689`
- 1h: commodity avg `0.0297` n `12`; crypto_alt avg `0.1432` n `228`; crypto_major avg `0.1815` n `8`; equity avg `-0.1811` n `74`; fx avg `0.0118` n `6`; index avg `-0.0478` n `23`; metal avg `-0.0974` n `18`; unknown avg `0.1233` n `689`
- 4h: commodity avg `-0.5802` n `12`; crypto_alt avg `-0.0748` n `228`; crypto_major avg `0.228` n `8`; equity avg `0.0397` n `74`; fx avg `0.0239` n `6`; index avg `0.0337` n `23`; metal avg `0.6477` n `18`; unknown avg `0.8264` n `689`
- 24h: commodity avg `-1.1382` n `12`; crypto_alt avg `2.967` n `228`; crypto_major avg `3.0864` n `8`; equity avg `1.5308` n `74`; fx avg `0.065` n `6`; index avg `0.9585` n `23`; metal avg `2.2564` n `18`; unknown avg `1.5864` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
