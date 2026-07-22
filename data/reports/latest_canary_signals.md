# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T23:07:30.901023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0122` n `12`; crypto_alt avg `-0.0419` n `230`; crypto_major avg `0.042` n `8`; equity avg `-0.0705` n `98`; fx avg `0.0033` n `6`; index avg `-0.0171` n `25`; metal avg `-0.0124` n `20`; unknown avg `-0.0241` n `773`
- 1h: commodity avg `-0.0081` n `12`; crypto_alt avg `-0.2277` n `230`; crypto_major avg `0.0297` n `8`; equity avg `-0.1913` n `98`; fx avg `-0.0007` n `6`; index avg `-0.0428` n `25`; metal avg `-0.045` n `20`; unknown avg `-0.016` n `773`
- 4h: commodity avg `0.1273` n `12`; crypto_alt avg `0.0373` n `230`; crypto_major avg `0.1369` n `8`; equity avg `-0.0716` n `98`; fx avg `-0.0227` n `6`; index avg `-0.0844` n `25`; metal avg `-0.1562` n `20`; unknown avg `0.1516` n `773`
- 24h: commodity avg `0.7011` n `12`; crypto_alt avg `-0.218` n `230`; crypto_major avg `-0.2512` n `8`; equity avg `-1.157` n `98`; fx avg `-0.054` n `6`; index avg `-0.2171` n `25`; metal avg `0.1269` n `20`; unknown avg `1.7265` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0944`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0799`, n `666`, weak_sample_signal
