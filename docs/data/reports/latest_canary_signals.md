# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T01:22:29.335096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1607` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0343` n `13`; crypto_alt avg `0.1079` n `237`; crypto_major avg `0.0999` n `8`; equity avg `0.2969` n `151`; fx avg `-0.001` n `6`; index avg `0.1009` n `26`; metal avg `-0.0006` n `20`; unknown avg `-0.0065` n `1194`
- 1h: commodity avg `0.0895` n `13`; crypto_alt avg `0.4174` n `237`; crypto_major avg `0.4106` n `8`; equity avg `0.5221` n `151`; fx avg `0.012` n `6`; index avg `0.1072` n `26`; metal avg `-0.0131` n `20`; unknown avg `0.0836` n `1136`
- 4h: commodity avg `-0.3939` n `13`; crypto_alt avg `3.1098` n `237`; crypto_major avg `2.4061` n `8`; equity avg `2.7631` n `151`; fx avg `0.062` n `6`; index avg `0.5437` n `26`; metal avg `0.2454` n `20`; unknown avg `4.7104` n `1046`
- 24h: commodity avg `-0.2892` n `13`; crypto_alt avg `-0.4927` n `237`; crypto_major avg `0.7225` n `8`; equity avg `2.2676` n `151`; fx avg `0.0035` n `6`; index avg `0.466` n `26`; metal avg `0.1931` n `20`; unknown avg `2.0053` n `903`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2032`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1383`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0951`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0937`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0781`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0671`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.061`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
