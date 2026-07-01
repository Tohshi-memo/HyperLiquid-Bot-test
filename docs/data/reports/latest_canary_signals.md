# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T15:37:27.017283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4387` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.3802` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6654` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0203` n `12`; crypto_alt avg `0.1438` n `228`; crypto_major avg `0.1239` n `8`; equity avg `-0.0633` n `88`; fx avg `-0.0138` n `6`; index avg `0.0009` n `25`; metal avg `-0.0179` n `20`; unknown avg `-0.1283` n `763`
- 1h: commodity avg `-0.1278` n `12`; crypto_alt avg `0.6205` n `228`; crypto_major avg `1.0087` n `8`; equity avg `0.4237` n `88`; fx avg `-0.0245` n `6`; index avg `0.0389` n `25`; metal avg `-0.3475` n `20`; unknown avg `-0.0624` n `763`
- 4h: commodity avg `-0.2057` n `12`; crypto_alt avg `1.7329` n `228`; crypto_major avg `2.233` n `8`; equity avg `-0.1472` n `88`; fx avg `-0.0924` n `6`; index avg `-0.1471` n `25`; metal avg `0.5676` n `20`; unknown avg `0.4685` n `763`
- 24h: commodity avg `-0.7146` n `12`; crypto_alt avg `2.3916` n `228`; crypto_major avg `2.3955` n `8`; equity avg `0.3074` n `88`; fx avg `-0.0459` n `6`; index avg `-0.2822` n `25`; metal avg `0.3142` n `20`; unknown avg `0.0475` n `741`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0481`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
