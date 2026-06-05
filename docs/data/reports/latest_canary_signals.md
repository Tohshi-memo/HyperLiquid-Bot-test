# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T06:07:25.331268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.6981` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.6685` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.5501` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.4109` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.7144` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_equity_divergence: score `-1.5127` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.7626` n `228`; crypto_major avg `-0.4104` n `8`; equity avg `-0.0315` n `74`; fx avg `-0.0118` n `6`; index avg `0.067` n `23`; metal avg `-0.1973` n `18`; unknown avg `0.8447` n `404`
- 1h: commodity avg `-0.0788` n `12`; crypto_alt avg `-1.7257` n `228`; crypto_major avg `-1.7507` n `8`; equity avg `-0.238` n `74`; fx avg `-0.0137` n `6`; index avg `-0.0363` n `23`; metal avg `-0.3457` n `18`; unknown avg `-0.5118` n `404`
- 4h: commodity avg `-0.0189` n `12`; crypto_alt avg `-2.838` n `228`; crypto_major avg `-2.717` n `8`; equity avg `-0.3061` n `74`; fx avg `-0.0551` n `6`; index avg `-0.0485` n `23`; metal avg `-0.1669` n `18`; unknown avg `-0.0059` n `404`
- 24h: commodity avg `-0.0951` n `12`; crypto_alt avg `-6.05` n `228`; crypto_major avg `-5.5465` n `8`; equity avg `-1.6401` n `73`; fx avg `0.1592` n `6`; index avg `-0.4613` n `23`; metal avg `-0.7716` n `18`; unknown avg `-1.8973` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
