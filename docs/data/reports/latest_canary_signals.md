# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T12:37:27.666978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.7016` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.6952` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5982` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0617` n `12`; crypto_alt avg `0.1331` n `231`; crypto_major avg `0.1626` n `8`; equity avg `-0.1547` n `122`; fx avg `0.0057` n `6`; index avg `-0.0413` n `25`; metal avg `-0.0473` n `20`; unknown avg `0.063` n `795`
- 1h: commodity avg `-0.1392` n `12`; crypto_alt avg `-0.7605` n `231`; crypto_major avg `-0.8182` n `8`; equity avg `-0.1795` n `122`; fx avg `-0.0088` n `6`; index avg `-0.0134` n `25`; metal avg `-0.0972` n `20`; unknown avg `-0.1417` n `795`
- 4h: commodity avg `-0.3768` n `12`; crypto_alt avg `-1.3074` n `231`; crypto_major avg `-1.6366` n `8`; equity avg `0.065` n `122`; fx avg `-0.0287` n `6`; index avg `0.0586` n `25`; metal avg `-0.0384` n `20`; unknown avg `-0.118` n `794`
- 24h: commodity avg `-0.9649` n `12`; crypto_alt avg `-1.2359` n `231`; crypto_major avg `-0.7931` n `8`; equity avg `0.4901` n `122`; fx avg `0.0269` n `6`; index avg `0.1269` n `25`; metal avg `-0.3534` n `20`; unknown avg `-0.3594` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
