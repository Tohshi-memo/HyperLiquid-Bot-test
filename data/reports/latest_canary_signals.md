# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T22:07:28.010905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6749` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4432` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.7779` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.006` n `13`; crypto_alt avg `-0.0009` n `235`; crypto_major avg `0.0363` n `8`; equity avg `0.0458` n `150`; fx avg `-0.009` n `6`; index avg `0.0039` n `26`; metal avg `-0.0` n `20`; unknown avg `0.1147` n `1075`
- 1h: commodity avg `-0.085` n `13`; crypto_alt avg `0.1879` n `235`; crypto_major avg `0.2098` n `8`; equity avg `0.0497` n `150`; fx avg `-0.0083` n `6`; index avg `-0.0049` n `26`; metal avg `0.0025` n `20`; unknown avg `0.1168` n `1075`
- 4h: commodity avg `-0.2064` n `13`; crypto_alt avg `3.083` n `235`; crypto_major avg `2.4685` n `8`; equity avg `0.6906` n `150`; fx avg `0.0207` n `6`; index avg `0.1095` n `26`; metal avg `0.0253` n `20`; unknown avg `1.0211` n `1007`
- 24h: commodity avg `0.5195` n `13`; crypto_alt avg `-2.4969` n `235`; crypto_major avg `-3.1646` n `8`; equity avg `-2.7094` n `150`; fx avg `0.0608` n `6`; index avg `-0.3718` n `26`; metal avg `-0.0038` n `20`; unknown avg `6.2755` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1817`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
