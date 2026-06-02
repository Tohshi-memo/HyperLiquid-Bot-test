# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T20:37:27.013253+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.92` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.8498` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.7365` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5138` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0703` n `12`; crypto_alt avg `0.5026` n `228`; crypto_major avg `0.1104` n `8`; equity avg `0.0044` n `69`; fx avg `-0.0094` n `6`; index avg `0.0389` n `23`; metal avg `0.0283` n `18`; unknown avg `0.318` n `422`
- 1h: commodity avg `-0.0824` n `12`; crypto_alt avg `1.0689` n `228`; crypto_major avg `0.2664` n `8`; equity avg `0.3781` n `69`; fx avg `-0.0056` n `6`; index avg `0.1983` n `23`; metal avg `0.1461` n `18`; unknown avg `0.4341` n `422`
- 4h: commodity avg `0.0189` n `12`; crypto_alt avg `-1.1259` n `228`; crypto_major avg `-1.584` n `8`; equity avg `0.2658` n `69`; fx avg `-0.024` n `6`; index avg `0.1525` n `23`; metal avg `-0.0702` n `18`; unknown avg `-0.7543` n `422`
- 24h: commodity avg `-0.0464` n `12`; crypto_alt avg `-4.1093` n `228`; crypto_major avg `-5.1558` n `8`; equity avg `0.8865` n `69`; fx avg `0.0803` n `6`; index avg `0.5661` n `23`; metal avg `0.4593` n `18`; unknown avg `-0.3898` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
