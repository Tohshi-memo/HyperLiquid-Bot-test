# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T03:52:27.514484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.2208` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.7085` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.006` n `13`; crypto_alt avg `0.1972` n `235`; crypto_major avg `0.0611` n `8`; equity avg `0.127` n `151`; fx avg `-0.0049` n `6`; index avg `0.0204` n `26`; metal avg `0.0696` n `20`; unknown avg `2.7149` n `1135`
- 1h: commodity avg `0.0342` n `13`; crypto_alt avg `1.2189` n `235`; crypto_major avg `0.6312` n `8`; equity avg `0.5384` n `151`; fx avg `0.0288` n `6`; index avg `0.0672` n `26`; metal avg `0.1059` n `20`; unknown avg `1.9199` n `1101`
- 4h: commodity avg `-0.0867` n `13`; crypto_alt avg `1.1641` n `235`; crypto_major avg `1.7669` n `8`; equity avg `-0.4539` n `151`; fx avg `0.1144` n `6`; index avg `-0.1961` n `26`; metal avg `0.0584` n `20`; unknown avg `4.4952` n `1095`
- 24h: commodity avg `0.6419` n `13`; crypto_alt avg `-4.3248` n `235`; crypto_major avg `-2.1718` n `8`; equity avg `-3.8208` n `151`; fx avg `0.0347` n `6`; index avg `-0.5709` n `26`; metal avg `-0.1793` n `20`; unknown avg `0.4039` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2086`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.195`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1317`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1118`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1076`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.092`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0882`, n `666`, weak_sample_signal
