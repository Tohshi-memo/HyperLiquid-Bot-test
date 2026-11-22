# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T10:07:27.519735+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3733` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.3026` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0135` n `13`; crypto_alt avg `0.3835` n `239`; crypto_major avg `0.3344` n `8`; equity avg `0.1692` n `166`; fx avg `-0.0154` n `6`; index avg `0.0274` n `27`; metal avg `0.0112` n `20`; unknown avg `42.0045` n `1197`
- 1h: commodity avg `0.0561` n `13`; crypto_alt avg `0.9905` n `239`; crypto_major avg `1.3648` n `8`; equity avg `0.4277` n `166`; fx avg `-0.0156` n `6`; index avg `0.054` n `27`; metal avg `0.0731` n `20`; unknown avg `405.362` n `1155`
- 4h: commodity avg `0.0574` n `13`; crypto_alt avg `1.8708` n `239`; crypto_major avg `2.4307` n `8`; equity avg `1.0111` n `166`; fx avg `-0.0364` n `6`; index avg `0.1161` n `27`; metal avg `0.1281` n `20`; unknown avg `89.5276` n `1137`
- 24h: commodity avg `0.0816` n `13`; crypto_alt avg `3.2582` n `239`; crypto_major avg `4.439` n `8`; equity avg `1.7205` n `166`; fx avg `-0.0134` n `6`; index avg `0.2097` n `27`; metal avg `0.1665` n `20`; unknown avg `-0.0312` n `1054`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
