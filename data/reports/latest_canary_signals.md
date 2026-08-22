# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T04:07:25.651388+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `4.3299` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `4.3193` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `4.2551` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0158` n `12`; crypto_alt avg `-0.1576` n `230`; crypto_major avg `-0.3309` n `8`; equity avg `-0.0295` n `121`; fx avg `-0.011` n `6`; index avg `-0.0269` n `25`; metal avg `0.005` n `20`; unknown avg `0.4057` n `794`
- 1h: commodity avg `0.0007` n `12`; crypto_alt avg `0.8225` n `230`; crypto_major avg `0.5194` n `8`; equity avg `-0.0339` n `121`; fx avg `-0.0017` n `6`; index avg `-0.0173` n `25`; metal avg `0.0012` n `20`; unknown avg `0.4682` n `793`
- 4h: commodity avg `-0.0125` n `12`; crypto_alt avg `4.3292` n `230`; crypto_major avg `4.3068` n `8`; equity avg `0.0517` n `121`; fx avg `0.0238` n `6`; index avg `-0.0174` n `25`; metal avg `-0.0231` n `20`; unknown avg `0.5086` n `793`
- 24h: commodity avg `0.1215` n `12`; crypto_alt avg `11.7946` n `230`; crypto_major avg `9.6742` n `8`; equity avg `0.3363` n `121`; fx avg `0.0443` n `6`; index avg `-0.0146` n `25`; metal avg `0.2142` n `20`; unknown avg `2.1994` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1924`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
