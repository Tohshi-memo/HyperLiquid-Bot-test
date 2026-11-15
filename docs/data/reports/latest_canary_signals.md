# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T04:22:24.099163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.1611` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.1052` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `1.7362` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0481` n `13`; crypto_alt avg `0.1343` n `239`; crypto_major avg `0.1667` n `8`; equity avg `-0.0291` n `162`; fx avg `0.0005` n `6`; index avg `-0.0053` n `27`; metal avg `0.0222` n `20`; unknown avg `-0.0882` n `1261`
- 1h: commodity avg `0.0398` n `13`; crypto_alt avg `-0.237` n `239`; crypto_major avg `-0.2937` n `8`; equity avg `-0.0379` n `162`; fx avg `0.0107` n `6`; index avg `-0.0043` n `27`; metal avg `-0.0008` n `20`; unknown avg `-0.1805` n `1251`
- 4h: commodity avg `0.0663` n `13`; crypto_alt avg `1.5023` n `239`; crypto_major avg `2.1715` n `8`; equity avg `0.4353` n `162`; fx avg `0.0139` n `6`; index avg `0.0049` n `27`; metal avg `0.0104` n `20`; unknown avg `1.1613` n `1248`
- 24h: commodity avg `0.0934` n `13`; crypto_alt avg `-5.1533` n `239`; crypto_major avg `-3.5039` n `8`; equity avg `-0.6807` n `162`; fx avg `0.0428` n `6`; index avg `-0.0642` n `27`; metal avg `-0.3606` n `20`; unknown avg `48.0517` n `1066`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1377`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1161`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1157`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1143`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1106`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0894`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0841`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `669`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0802`, n `669`, weak_sample_signal
