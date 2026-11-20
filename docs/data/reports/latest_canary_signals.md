# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T17:22:42.800073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.4291` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.1725` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-3.1445` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.07` n `13`; crypto_alt avg `-0.0454` n `239`; crypto_major avg `-0.086` n `8`; equity avg `0.0251` n `166`; fx avg `0.0046` n `6`; index avg `-0.0291` n `27`; metal avg `-0.0794` n `20`; unknown avg `1.1864` n `1259`
- 1h: commodity avg `0.1809` n `13`; crypto_alt avg `-0.6894` n `239`; crypto_major avg `-0.5483` n `8`; equity avg `-1.4885` n `166`; fx avg `0.0239` n `6`; index avg `-0.1733` n `27`; metal avg `-0.1909` n `20`; unknown avg `318.1295` n `1257`
- 4h: commodity avg `-0.0468` n `13`; crypto_alt avg `-3.3303` n `239`; crypto_major avg `-3.4759` n `8`; equity avg `-3.1651` n `166`; fx avg `-0.0038` n `6`; index avg `-0.3034` n `27`; metal avg `-0.3314` n `20`; unknown avg `256.2558` n `1247`
- 24h: commodity avg `-0.214` n `13`; crypto_alt avg `-6.066` n `239`; crypto_major avg `-6.4078` n `8`; equity avg `-8.7755` n `166`; fx avg `0.0248` n `6`; index avg `-0.7869` n `27`; metal avg `-1.3108` n `20`; unknown avg `39.6881` n `1155`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1531`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
