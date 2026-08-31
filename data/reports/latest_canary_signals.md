# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T04:22:26.190345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0233` n `12`; crypto_alt avg `-0.3096` n `232`; crypto_major avg `-0.2354` n `8`; equity avg `0.018` n `128`; fx avg `0.0077` n `6`; index avg `0.005` n `26`; metal avg `0.0331` n `20`; unknown avg `0.0107` n `793`
- 1h: commodity avg `0.046` n `12`; crypto_alt avg `-0.1442` n `231`; crypto_major avg `-0.2877` n `8`; equity avg `-0.0662` n `128`; fx avg `-0.0124` n `6`; index avg `-0.0102` n `26`; metal avg `-0.0754` n `20`; unknown avg `-0.014` n `791`
- 4h: commodity avg `0.2607` n `12`; crypto_alt avg `0.2491` n `231`; crypto_major avg `-0.6711` n `8`; equity avg `-0.1901` n `128`; fx avg `-0.0755` n `6`; index avg `0.0374` n `26`; metal avg `-0.3051` n `20`; unknown avg `-0.2833` n `779`
- 24h: commodity avg `0.393` n `12`; crypto_alt avg `-0.4754` n `231`; crypto_major avg `-2.2601` n `8`; equity avg `-1.1851` n `128`; fx avg `-0.0514` n `6`; index avg `-0.2171` n `26`; metal avg `-0.3928` n `20`; unknown avg `-0.556` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
