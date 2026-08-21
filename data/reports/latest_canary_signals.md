# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T09:49:14.619143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7243` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.6091` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.0321` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `0.4556` n `230`; crypto_major avg `0.5102` n `8`; equity avg `0.068` n `121`; fx avg `0.0118` n `6`; index avg `-0.0039` n `25`; metal avg `-0.0253` n `20`; unknown avg `0.098` n `793`
- 1h: commodity avg `0.0716` n `12`; crypto_alt avg `-0.5802` n `230`; crypto_major avg `-0.4982` n `8`; equity avg `0.0533` n `121`; fx avg `0.0251` n `6`; index avg `-0.0267` n `25`; metal avg `-0.0653` n `20`; unknown avg `0.1363` n `793`
- 4h: commodity avg `0.0873` n `12`; crypto_alt avg `2.8841` n `230`; crypto_major avg `2.8116` n `8`; equity avg `0.7795` n `121`; fx avg `0.0061` n `6`; index avg `0.0413` n `25`; metal avg `0.2025` n `20`; unknown avg `0.4201` n `777`
- 24h: commodity avg `0.0366` n `12`; crypto_alt avg `7.4783` n `230`; crypto_major avg `7.9329` n `8`; equity avg `0.6219` n `121`; fx avg `-0.0812` n `6`; index avg `0.0123` n `25`; metal avg `0.8664` n `20`; unknown avg `2.5496` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2156`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
