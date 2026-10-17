# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T06:07:28.062620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0277` n `13`; crypto_alt avg `0.0717` n `236`; crypto_major avg `0.0213` n `8`; equity avg `0.034` n `151`; fx avg `-0.0005` n `6`; index avg `0.0017` n `26`; metal avg `0.0034` n `20`; unknown avg `0.3975` n `1175`
- 1h: commodity avg `-0.0365` n `13`; crypto_alt avg `-0.1909` n `236`; crypto_major avg `-0.0375` n `8`; equity avg `0.0107` n `151`; fx avg `0.0016` n `6`; index avg `0.026` n `26`; metal avg `-0.0138` n `20`; unknown avg `0.7437` n `1175`
- 4h: commodity avg `-0.024` n `13`; crypto_alt avg `0.1161` n `236`; crypto_major avg `0.1356` n `8`; equity avg `0.0772` n `151`; fx avg `0.011` n `6`; index avg `0.0503` n `26`; metal avg `0.0193` n `20`; unknown avg `0.6348` n `1169`
- 24h: commodity avg `0.6472` n `13`; crypto_alt avg `-1.3739` n `236`; crypto_major avg `-1.0386` n `8`; equity avg `-3.9144` n `151`; fx avg `0.0415` n `6`; index avg `-0.5953` n `26`; metal avg `-0.1868` n `20`; unknown avg `40.4768` n `912`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1792`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1227`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1159`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0762`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
