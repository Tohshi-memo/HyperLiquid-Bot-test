# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T04:52:28.645173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.9723` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `3.6571` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `3.4895` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0261` n `13`; crypto_alt avg `0.1636` n `235`; crypto_major avg `-0.0187` n `8`; equity avg `-0.0483` n `151`; fx avg `-0.002` n `6`; index avg `-0.0218` n `26`; metal avg `0.0147` n `20`; unknown avg `-0.256` n `1133`
- 1h: commodity avg `-0.1064` n `13`; crypto_alt avg `0.5506` n `235`; crypto_major avg `0.192` n `8`; equity avg `-0.1628` n `151`; fx avg `-0.0232` n `6`; index avg `-0.0434` n `26`; metal avg `0.0543` n `20`; unknown avg `-0.3624` n `1125`
- 4h: commodity avg `-0.2331` n `13`; crypto_alt avg `4.5777` n `235`; crypto_major avg `3.7392` n `8`; equity avg `0.0821` n `151`; fx avg `0.0853` n `6`; index avg `-0.1179` n `26`; metal avg `0.2497` n `20`; unknown avg `7.179` n `1093`
- 24h: commodity avg `0.4944` n `13`; crypto_alt avg `-4.3472` n `235`; crypto_major avg `-2.6374` n `8`; equity avg `-4.069` n `151`; fx avg `-0.0136` n `6`; index avg `-0.621` n `26`; metal avg `-0.0823` n `20`; unknown avg `0.6514` n `857`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2037`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1919`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1361`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1152`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1036`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0822`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0819`, n `666`, weak_sample_signal
