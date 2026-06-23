# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T08:37:30.647859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0015` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.5907` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.5052` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.349` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0494` n `12`; crypto_alt avg `-0.0096` n `228`; crypto_major avg `-0.071` n `8`; equity avg `0.0685` n `86`; fx avg `0.0032` n `6`; index avg `0.0271` n `23`; metal avg `-0.0405` n `20`; unknown avg `-0.0686` n `764`
- 1h: commodity avg `0.1803` n `12`; crypto_alt avg `-1.4826` n `228`; crypto_major avg `-1.4219` n `8`; equity avg `-0.6536` n `86`; fx avg `-0.0293` n `6`; index avg `-0.0729` n `23`; metal avg `-0.172` n `20`; unknown avg `-0.3835` n `764`
- 4h: commodity avg `0.0171` n `12`; crypto_alt avg `-3.2697` n `228`; crypto_major avg `-2.9844` n `8`; equity avg `-1.6888` n `86`; fx avg `-0.0189` n `6`; index avg `-0.3937` n `23`; metal avg `-0.4792` n `20`; unknown avg `0.0479` n `604`
- 24h: commodity avg `-0.5689` n `12`; crypto_alt avg `-3.9836` n `228`; crypto_major avg `-3.9165` n `8`; equity avg `-4.5111` n `85`; fx avg `-0.0759` n `6`; index avg `-0.8161` n `23`; metal avg `-1.4681` n `18`; unknown avg `0.6404` n `583`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
