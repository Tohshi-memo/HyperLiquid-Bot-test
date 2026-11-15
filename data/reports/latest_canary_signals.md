# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T03:07:42.005462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `4.0939` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `4.0672` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.3608` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_commodity_crypto_divergence: score `2.6878` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `2.5584` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `2.1261` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0124` n `13`; crypto_alt avg `0.3718` n `239`; crypto_major avg `0.5703` n `8`; equity avg `0.09` n `162`; fx avg `-0.0086` n `6`; index avg `0.0019` n `27`; metal avg `0.0283` n `20`; unknown avg `0.377` n `1257`
- 1h: commodity avg `-0.0053` n `13`; crypto_alt avg `1.9145` n `239`; crypto_major avg `2.6825` n `8`; equity avg `0.5564` n `162`; fx avg `0.0077` n `6`; index avg `0.0316` n `27`; metal avg `0.1241` n `20`; unknown avg `18.4153` n `1259`
- 4h: commodity avg `0.0634` n `13`; crypto_alt avg `3.6023` n `239`; crypto_major avg `4.1306` n `8`; equity avg `0.7698` n `162`; fx avg `-0.005` n `6`; index avg `0.0336` n `27`; metal avg `0.0367` n `20`; unknown avg `3.1072` n `1250`
- 24h: commodity avg `0.0099` n `13`; crypto_alt avg `-5.4736` n `239`; crypto_major avg `-4.3497` n `8`; equity avg `-0.766` n `162`; fx avg `0.0333` n `6`; index avg `-0.07` n `27`; metal avg `-0.4056` n `20`; unknown avg `48.0238` n `1070`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
