# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T04:22:30.806148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.8647` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `2.6355` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `2.4621` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.011` n `13`; crypto_alt avg `0.0838` n `235`; crypto_major avg `-0.0019` n `8`; equity avg `-0.1007` n `151`; fx avg `-0.0064` n `6`; index avg `-0.0044` n `26`; metal avg `0.0004` n `20`; unknown avg `-0.2488` n `1135`
- 1h: commodity avg `-0.1281` n `13`; crypto_alt avg `0.8607` n `235`; crypto_major avg `0.5689` n `8`; equity avg `0.339` n `151`; fx avg `-0.0202` n `6`; index avg `0.0421` n `26`; metal avg `0.0984` n `20`; unknown avg `0.4592` n `1095`
- 4h: commodity avg `-0.2381` n `13`; crypto_alt avg `2.2795` n `235`; crypto_major avg `2.6266` n `8`; equity avg `-0.0089` n `151`; fx avg `0.1079` n `6`; index avg `-0.1196` n `26`; metal avg `0.1645` n `20`; unknown avg `6.4557` n `1095`
- 24h: commodity avg `0.497` n `13`; crypto_alt avg `-4.1218` n `235`; crypto_major avg `-2.1623` n `8`; equity avg `-3.7117` n `151`; fx avg `0.0118` n `6`; index avg `-0.5612` n `26`; metal avg `-0.128` n `20`; unknown avg `0.5707` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2036`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1912`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1377`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1167`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1052`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0838`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.083`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
