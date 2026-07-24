# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T11:22:28.619424+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `-0.0404` n `230`; crypto_major avg `-0.0562` n `8`; equity avg `-0.0576` n `100`; fx avg `0.0063` n `6`; index avg `-0.0056` n `25`; metal avg `-0.01` n `20`; unknown avg `-0.004` n `773`
- 1h: commodity avg `0.0416` n `12`; crypto_alt avg `-0.0885` n `230`; crypto_major avg `-0.031` n `8`; equity avg `-0.1376` n `100`; fx avg `0.0039` n `6`; index avg `-0.0125` n `25`; metal avg `-0.003` n `20`; unknown avg `-0.107` n `773`
- 4h: commodity avg `-0.1175` n `12`; crypto_alt avg `-0.7831` n `230`; crypto_major avg `-0.8134` n `8`; equity avg `0.0312` n `100`; fx avg `-0.0683` n `6`; index avg `0.0304` n `25`; metal avg `0.1205` n `20`; unknown avg `0.1214` n `772`
- 24h: commodity avg `-0.2242` n `12`; crypto_alt avg `-1.4257` n `230`; crypto_major avg `-1.8802` n `8`; equity avg `-1.587` n `99`; fx avg `-0.1336` n `6`; index avg `-0.4097` n `25`; metal avg `-0.2654` n `20`; unknown avg `0.1838` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1009`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0905`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0841`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
