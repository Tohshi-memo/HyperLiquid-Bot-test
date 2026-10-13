# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T03:37:26.565902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.3396` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.7094` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0088` n `13`; crypto_alt avg `0.5038` n `235`; crypto_major avg `0.4795` n `8`; equity avg `0.223` n `151`; fx avg `0.0009` n `6`; index avg `0.0341` n `26`; metal avg `0.0079` n `20`; unknown avg `0.9169` n `1103`
- 1h: commodity avg `0.0063` n `13`; crypto_alt avg `0.9046` n `235`; crypto_major avg `0.6` n `8`; equity avg `0.2635` n `151`; fx avg `0.0734` n `6`; index avg `0.0308` n `26`; metal avg `0.0323` n `20`; unknown avg `0.9062` n `1101`
- 4h: commodity avg `-0.1427` n `13`; crypto_alt avg `1.0442` n `235`; crypto_major avg `1.6748` n `8`; equity avg `-0.6648` n `151`; fx avg `0.1214` n `6`; index avg `-0.2426` n `26`; metal avg `-0.0346` n `20`; unknown avg `5.1438` n `1095`
- 24h: commodity avg `0.645` n `13`; crypto_alt avg `-4.6015` n `235`; crypto_major avg `-2.2963` n `8`; equity avg `-3.9809` n `151`; fx avg `0.0493` n `6`; index avg `-0.5979` n `26`; metal avg `-0.2366` n `20`; unknown avg `0.6242` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2118`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1973`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1327`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1125`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1074`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0972`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0952`, n `666`, weak_sample_signal
