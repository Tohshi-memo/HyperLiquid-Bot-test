# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T05:07:25.565822+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.3348` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.3339` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.7078` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0081` n `13`; crypto_alt avg `-0.2829` n `239`; crypto_major avg `-0.5507` n `8`; equity avg `-0.0565` n `162`; fx avg `0.0023` n `6`; index avg `-0.0031` n `27`; metal avg `-0.0217` n `20`; unknown avg `130.7599` n `1257`
- 1h: commodity avg `0.0393` n `13`; crypto_alt avg `0.0235` n `239`; crypto_major avg `-0.2166` n `8`; equity avg `-0.1007` n `162`; fx avg `-0.003` n `6`; index avg `-0.0131` n `27`; metal avg `-0.0552` n `20`; unknown avg `104.2169` n `1255`
- 4h: commodity avg `0.0599` n `13`; crypto_alt avg `2.4732` n `239`; crypto_major avg `3.3938` n `8`; equity avg `0.686` n `162`; fx avg `0.0117` n `6`; index avg `0.0393` n `27`; metal avg `0.059` n `20`; unknown avg `110.0622` n `1238`
- 24h: commodity avg `0.0804` n `13`; crypto_alt avg `-5.1639` n `239`; crypto_major avg `-3.9408` n `8`; equity avg `-0.7178` n `162`; fx avg `0.0401` n `6`; index avg `-0.071` n `27`; metal avg `-0.4432` n `20`; unknown avg `53.7459` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
