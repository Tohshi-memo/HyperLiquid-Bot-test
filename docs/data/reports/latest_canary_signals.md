# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T09:52:31.398801+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2607` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.2316` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.1561` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.9231` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0095` n `12`; crypto_alt avg `0.0489` n `228`; crypto_major avg `0.0449` n `8`; equity avg `-0.0156` n `86`; fx avg `-0.021` n `6`; index avg `-0.0149` n `23`; metal avg `0.0003` n `20`; unknown avg `-0.0405` n `764`
- 1h: commodity avg `-0.1159` n `12`; crypto_alt avg `0.2446` n `228`; crypto_major avg `0.0449` n `8`; equity avg `0.3841` n `86`; fx avg `-0.0298` n `6`; index avg `0.0532` n `23`; metal avg `0.1936` n `20`; unknown avg `-0.2491` n `764`
- 4h: commodity avg `-0.0442` n `12`; crypto_alt avg `-2.2146` n `228`; crypto_major avg `-2.3049` n `8`; equity avg `-0.3818` n `86`; fx avg `-0.0441` n `6`; index avg `-0.1488` n `23`; metal avg `-0.0733` n `20`; unknown avg `-0.5638` n `604`
- 24h: commodity avg `-0.6735` n `12`; crypto_alt avg `-3.748` n `228`; crypto_major avg `-4.0052` n `8`; equity avg `-4.222` n `85`; fx avg `-0.1326` n `6`; index avg `-0.7938` n `23`; metal avg `-1.4072` n `18`; unknown avg `0.6506` n `583`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
