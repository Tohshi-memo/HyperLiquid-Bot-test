# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T08:22:35.982095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.9893` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.5715` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.5448` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.437` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0277` n `12`; crypto_alt avg `-1.1858` n `228`; crypto_major avg `-0.9855` n `8`; equity avg `-0.4436` n `86`; fx avg `-0.0155` n `6`; index avg `-0.0335` n `23`; metal avg `0.062` n `20`; unknown avg `0.2205` n `764`
- 1h: commodity avg `0.1902` n `12`; crypto_alt avg `-1.5694` n `228`; crypto_major avg `-1.5512` n `8`; equity avg `-0.9411` n `86`; fx avg `-0.0515` n `6`; index avg `-0.1142` n `23`; metal avg `-0.228` n `20`; unknown avg `-0.3193` n `620`
- 4h: commodity avg `0.0063` n `12`; crypto_alt avg `-3.3106` n `228`; crypto_major avg `-2.983` n `8`; equity avg `-1.7983` n `86`; fx avg `-0.0324` n `6`; index avg `-0.4115` n `23`; metal avg `-0.4382` n `20`; unknown avg `0.124` n `604`
- 24h: commodity avg `-0.7391` n `12`; crypto_alt avg `-4.1742` n `228`; crypto_major avg `-4.1381` n `8`; equity avg `-4.5461` n `85`; fx avg `-0.0757` n `6`; index avg `-0.8435` n `23`; metal avg `-1.4141` n `18`; unknown avg `0.7118` n `583`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.157`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
