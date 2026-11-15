# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T04:07:26.036511+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.6104` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.5793` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.1294` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `-0.092` n `239`; crypto_major avg `-0.1114` n `8`; equity avg `0.0108` n `162`; fx avg `0.0035` n `6`; index avg `0.0098` n `27`; metal avg `0.0276` n `20`; unknown avg `0.0831` n `1249`
- 1h: commodity avg `-0.015` n `13`; crypto_alt avg `-0.229` n `239`; crypto_major avg `-0.2873` n `8`; equity avg `0.032` n `162`; fx avg `0.008` n `6`; index avg `0.004` n `27`; metal avg `-0.0107` n `20`; unknown avg `-0.0361` n `1251`
- 4h: commodity avg `0.0221` n `13`; crypto_alt avg `1.8127` n `239`; crypto_major avg `2.6014` n `8`; equity avg `0.472` n `162`; fx avg `0.0142` n `6`; index avg `0.0102` n `27`; metal avg `-0.009` n `20`; unknown avg `1.4239` n `1246`
- 24h: commodity avg `0.0472` n `13`; crypto_alt avg `-5.1374` n `239`; crypto_major avg `-3.5043` n `8`; equity avg `-0.6143` n `162`; fx avg `0.0484` n `6`; index avg `-0.0553` n `27`; metal avg `-0.3705` n `20`; unknown avg `48.3139` n `1066`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1399`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.116`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1156`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1102`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0834`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0804`, n `669`, weak_sample_signal
