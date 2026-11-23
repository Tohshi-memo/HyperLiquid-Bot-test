# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T14:22:28.279859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `5.5258` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `4.9669` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `4.654` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `4.3523` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0247` n `13`; crypto_alt avg `1.6186` n `239`; crypto_major avg `1.6455` n `8`; equity avg `0.9817` n `166`; fx avg `0.0212` n `6`; index avg `0.0318` n `27`; metal avg `0.1145` n `20`; unknown avg `8.9716` n `1264`
- 1h: commodity avg `0.0296` n `13`; crypto_alt avg `4.026` n `239`; crypto_major avg `4.9965` n `8`; equity avg `5.7277` n `166`; fx avg `-0.0531` n `6`; index avg `0.5551` n `27`; metal avg `0.6442` n `20`; unknown avg `319.8383` n `1262`
- 4h: commodity avg `-0.2676` n `13`; crypto_alt avg `3.872` n `239`; crypto_major avg `5.2582` n `8`; equity avg `5.2394` n `166`; fx avg `-0.1059` n `6`; index avg `0.5189` n `27`; metal avg `0.6042` n `20`; unknown avg `8.7291` n `1252`
- 24h: commodity avg `-0.973` n `13`; crypto_alt avg `4.6681` n `239`; crypto_major avg `6.4804` n `8`; equity avg `7.6316` n `166`; fx avg `0.0875` n `6`; index avg `0.619` n `27`; metal avg `1.0263` n `20`; unknown avg `8.3972` n `1059`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
