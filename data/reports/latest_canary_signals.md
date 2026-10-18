# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T23:49:10.932013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9531` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2447` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0336` n `13`; crypto_alt avg `0.1894` n `237`; crypto_major avg `0.014` n `8`; equity avg `0.1344` n `151`; fx avg `0.0101` n `6`; index avg `0.0185` n `26`; metal avg `0.0396` n `20`; unknown avg `0.108` n `1194`
- 1h: commodity avg `-0.0773` n `13`; crypto_alt avg `0.686` n `237`; crypto_major avg `0.3271` n `8`; equity avg `0.2049` n `151`; fx avg `0.0058` n `6`; index avg `0.0051` n `26`; metal avg `0.0571` n `20`; unknown avg `2.5585` n `1192`
- 4h: commodity avg `-0.4273` n `13`; crypto_alt avg `3.1545` n `237`; crypto_major avg `2.5258` n `8`; equity avg `1.7598` n `151`; fx avg `0.011` n `6`; index avg `0.323` n `26`; metal avg `0.2811` n `20`; unknown avg `15.0128` n `1090`
- 24h: commodity avg `-0.3611` n `13`; crypto_alt avg `-1.3516` n `236`; crypto_major avg `0.6544` n `8`; equity avg `1.1321` n `151`; fx avg `-0.0125` n `6`; index avg `0.2434` n `26`; metal avg `0.2466` n `20`; unknown avg `6.4592` n `961`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2007`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1363`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0904`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.087`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0804`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0697`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.066`, n `666`, weak_sample_signal
