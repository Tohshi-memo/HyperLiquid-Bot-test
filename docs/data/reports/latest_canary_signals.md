# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T01:52:32.355521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5834` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.8802` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0001` n `13`; crypto_alt avg `0.1069` n `237`; crypto_major avg `0.1001` n `8`; equity avg `-0.0261` n `151`; fx avg `0.0017` n `6`; index avg `-0.0129` n `26`; metal avg `0.032` n `20`; unknown avg `-0.1092` n `1194`
- 1h: commodity avg `0.0296` n `13`; crypto_alt avg `0.2893` n `237`; crypto_major avg `0.1455` n `8`; equity avg `0.35` n `151`; fx avg `-0.0206` n `6`; index avg `0.0802` n `26`; metal avg `0.0653` n `20`; unknown avg `-0.1706` n `1192`
- 4h: commodity avg `-0.401` n `13`; crypto_alt avg `2.9697` n `237`; crypto_major avg `2.1824` n `8`; equity avg `2.2839` n `151`; fx avg `0.0282` n `6`; index avg `0.4413` n `26`; metal avg `0.3022` n `20`; unknown avg `4.7435` n `1118`
- 24h: commodity avg `-0.3871` n `13`; crypto_alt avg `-0.277` n `237`; crypto_major avg `0.6771` n `8`; equity avg `2.1477` n `151`; fx avg `-0.0202` n `6`; index avg `0.4053` n `26`; metal avg `0.2608` n `20`; unknown avg `2.1278` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2006`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1397`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1056`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0853`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0652`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.06`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
