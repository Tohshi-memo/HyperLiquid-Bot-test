# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T17:07:39.846828+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0916` n `12`; crypto_alt avg `-0.044` n `230`; crypto_major avg `-0.0249` n `8`; equity avg `-0.2444` n `102`; fx avg `-0.0176` n `6`; index avg `-0.0577` n `25`; metal avg `-0.0494` n `20`; unknown avg `-0.0607` n `774`
- 1h: commodity avg `-0.1477` n `12`; crypto_alt avg `0.359` n `230`; crypto_major avg `0.5038` n `8`; equity avg `-0.0051` n `102`; fx avg `-0.0408` n `6`; index avg `-0.0879` n `25`; metal avg `-0.0636` n `20`; unknown avg `0.219` n `774`
- 4h: commodity avg `-0.32` n `12`; crypto_alt avg `-1.2686` n `230`; crypto_major avg `-1.0753` n `8`; equity avg `-2.5328` n `102`; fx avg `-0.0935` n `6`; index avg `-0.6298` n `25`; metal avg `0.0045` n `20`; unknown avg `-0.3539` n `774`
- 24h: commodity avg `-0.6702` n `12`; crypto_alt avg `-1.145` n `230`; crypto_major avg `-0.4456` n `8`; equity avg `-1.9109` n `102`; fx avg `-0.0006` n `6`; index avg `-0.5684` n `25`; metal avg `0.1891` n `20`; unknown avg `-0.1996` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1955`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
