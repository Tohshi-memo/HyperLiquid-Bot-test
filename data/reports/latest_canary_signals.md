# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T09:07:28.744884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5253` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.3696` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.3245` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.5756` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.0534` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0729` n `12`; crypto_alt avg `0.0883` n `228`; crypto_major avg `0.0136` n `8`; equity avg `0.2052` n `86`; fx avg `-0.0052` n `6`; index avg `0.001` n `23`; metal avg `0.0289` n `20`; unknown avg `-0.103` n `764`
- 1h: commodity avg `-0.0244` n `12`; crypto_alt avg `-0.911` n `228`; crypto_major avg `-1.0592` n `8`; equity avg `-0.1146` n `86`; fx avg `-0.0144` n `6`; index avg `-0.0058` n `23`; metal avg `0.0857` n `20`; unknown avg `0.1184` n `764`
- 4h: commodity avg `-0.1483` n `12`; crypto_alt avg `-2.6579` n `228`; crypto_major avg `-2.6736` n `8`; equity avg `-1.098` n `86`; fx avg `-0.0248` n `6`; index avg `-0.304` n `23`; metal avg `-0.3491` n `20`; unknown avg `-0.6088` n `604`
- 24h: commodity avg `-0.6234` n `12`; crypto_alt avg `-3.9819` n `228`; crypto_major avg `-4.107` n `8`; equity avg `-4.417` n `85`; fx avg `-0.0926` n `6`; index avg `-0.8507` n `23`; metal avg `-1.5899` n `18`; unknown avg `0.7296` n `583`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
