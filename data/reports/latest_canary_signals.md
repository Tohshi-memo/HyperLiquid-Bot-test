# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T04:37:36.064031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8339` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.8329` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.3955` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0108` n `13`; crypto_alt avg `0.229` n `235`; crypto_major avg `0.183` n `8`; equity avg `-0.0954` n `151`; fx avg `-0.005` n `6`; index avg `-0.0094` n `26`; metal avg `0.0187` n `20`; unknown avg `0.052` n `1135`
- 1h: commodity avg `-0.1261` n `13`; crypto_alt avg `0.5852` n `235`; crypto_major avg `0.2721` n `8`; equity avg `0.012` n `151`; fx avg `-0.0261` n `6`; index avg `-0.0014` n `26`; metal avg `0.1092` n `20`; unknown avg `0.6372` n `1127`
- 4h: commodity avg `-0.2462` n `13`; crypto_alt avg `2.5017` n `235`; crypto_major avg `2.5877` n `8`; equity avg `-0.2452` n `151`; fx avg `0.1207` n `6`; index avg `-0.1354` n `26`; metal avg `0.1922` n `20`; unknown avg `5.4558` n `1095`
- 24h: commodity avg `0.4938` n `13`; crypto_alt avg `-4.4491` n `235`; crypto_major avg `-2.4275` n `8`; equity avg `-3.998` n `151`; fx avg `0.005` n `6`; index avg `-0.6042` n `26`; metal avg `-0.1154` n `20`; unknown avg `0.7333` n `855`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2032`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1909`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1387`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1173`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1039`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0835`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0826`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
