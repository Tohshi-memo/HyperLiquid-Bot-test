# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T08:07:52.361463+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0186` n `12`; crypto_alt avg `0.0578` n `228`; crypto_major avg `0.0184` n `8`; equity avg `0.0475` n `88`; fx avg `-0.0096` n `6`; index avg `0.0228` n `23`; metal avg `0.0232` n `20`; unknown avg `0.0488` n `765`
- 1h: commodity avg `0.04` n `12`; crypto_alt avg `-0.1007` n `228`; crypto_major avg `-0.023` n `8`; equity avg `-0.0477` n `88`; fx avg `0.0309` n `6`; index avg `-0.0223` n `23`; metal avg `0.0181` n `20`; unknown avg `0.1693` n `765`
- 4h: commodity avg `0.0736` n `12`; crypto_alt avg `-0.0292` n `228`; crypto_major avg `0.1118` n `8`; equity avg `-0.047` n `88`; fx avg `0.067` n `6`; index avg `-0.0367` n `23`; metal avg `0.6488` n `20`; unknown avg `-0.6057` n `737`
- 24h: commodity avg `0.0165` n `12`; crypto_alt avg `-0.3666` n `228`; crypto_major avg `0.8536` n `8`; equity avg `1.5324` n `88`; fx avg `0.178` n `6`; index avg `0.1613` n `23`; metal avg `-0.0478` n `20`; unknown avg `8.5775` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
