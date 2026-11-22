# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T10:37:29.400678+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0195` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9422` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0118` n `13`; crypto_alt avg `-0.0015` n `239`; crypto_major avg `-0.1658` n `8`; equity avg `-0.0385` n `166`; fx avg `-0.0039` n `6`; index avg `-0.0106` n `27`; metal avg `0.0043` n `20`; unknown avg `316.7177` n `1263`
- 1h: commodity avg `0.0211` n `13`; crypto_alt avg `0.8658` n `239`; crypto_major avg `0.8501` n `8`; equity avg `0.4068` n `166`; fx avg `-0.0086` n `6`; index avg `0.0495` n `27`; metal avg `0.0441` n `20`; unknown avg `86.7967` n `1155`
- 4h: commodity avg `0.0537` n `13`; crypto_alt avg `1.6989` n `239`; crypto_major avg `2.0732` n `8`; equity avg `0.9869` n `166`; fx avg `-0.0354` n `6`; index avg `0.11` n `27`; metal avg `0.131` n `20`; unknown avg `88.5826` n `1141`
- 24h: commodity avg `0.0727` n `13`; crypto_alt avg `3.3752` n `239`; crypto_major avg `4.1843` n `8`; equity avg `1.8693` n `166`; fx avg `0.0138` n `6`; index avg `0.229` n `27`; metal avg `0.1452` n `20`; unknown avg `0.0192` n `1054`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
