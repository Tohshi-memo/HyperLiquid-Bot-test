# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T09:22:35.396627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.4399` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.2968` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.2624` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.7363` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.021` n `12`; crypto_alt avg `0.2153` n `228`; crypto_major avg `0.1121` n `8`; equity avg `0.1739` n `86`; fx avg `0.001` n `6`; index avg `0.0547` n `23`; metal avg `0.0685` n `20`; unknown avg `-0.0561` n `764`
- 1h: commodity avg `-0.031` n `12`; crypto_alt avg `0.4964` n `228`; crypto_major avg `0.0379` n `8`; equity avg `0.5083` n `86`; fx avg `0.0021` n `6`; index avg `0.0826` n `23`; metal avg `0.0921` n `20`; unknown avg `-0.3502` n `764`
- 4h: commodity avg `-0.0714` n `12`; crypto_alt avg `-2.3156` n `228`; crypto_major avg `-2.5113` n `8`; equity avg `-0.775` n `86`; fx avg `-0.0196` n `6`; index avg `-0.2145` n `23`; metal avg `-0.2489` n `20`; unknown avg `-0.637` n `604`
- 24h: commodity avg `-0.5959` n `12`; crypto_alt avg `-3.6641` n `228`; crypto_major avg `-3.9097` n `8`; equity avg `-4.2318` n `85`; fx avg `-0.0993` n `6`; index avg `-0.7969` n `23`; metal avg `-1.4968` n `18`; unknown avg `0.6839` n `583`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
