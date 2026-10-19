# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T00:52:29.471778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.3038` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5709` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0025` n `13`; crypto_alt avg `0.3761` n `237`; crypto_major avg `0.3078` n `8`; equity avg `0.3205` n `151`; fx avg `-0.0107` n `6`; index avg `0.039` n `26`; metal avg `0.0033` n `20`; unknown avg `0.4318` n `1158`
- 1h: commodity avg `-0.0254` n `13`; crypto_alt avg `0.296` n `237`; crypto_major avg `0.3256` n `8`; equity avg `0.6138` n `151`; fx avg `0.0158` n `6`; index avg `0.0902` n `26`; metal avg `-0.029` n `20`; unknown avg `-0.1267` n `1128`
- 4h: commodity avg `-0.4681` n `13`; crypto_alt avg `3.5219` n `237`; crypto_major avg `2.8357` n `8`; equity avg `2.4296` n `151`; fx avg `0.019` n `6`; index avg `0.4326` n `26`; metal avg `0.2648` n `20`; unknown avg `6.8984` n `1040`
- 24h: commodity avg `-0.3554` n `13`; crypto_alt avg `-0.396` n `237`; crypto_major avg `0.7912` n `8`; equity avg `1.8548` n `151`; fx avg `-0.0005` n `6`; index avg `0.3364` n `26`; metal avg `0.1957` n `20`; unknown avg `1.8534` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2052`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1384`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0879`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0826`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0673`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
