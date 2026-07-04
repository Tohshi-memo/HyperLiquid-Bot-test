# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T00:52:29.907629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.9` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0022` n `12`; crypto_alt avg `-0.1556` n `229`; crypto_major avg `0.0275` n `8`; equity avg `0.1044` n `88`; fx avg `-0.0015` n `6`; index avg `0.001` n `25`; metal avg `0.002` n `20`; unknown avg `-0.6169` n `765`
- 1h: commodity avg `0.0423` n `12`; crypto_alt avg `-0.2175` n `229`; crypto_major avg `0.1608` n `8`; equity avg `0.1256` n `88`; fx avg `0.0063` n `6`; index avg `-0.0391` n `25`; metal avg `-0.0318` n `20`; unknown avg `-0.2043` n `765`
- 4h: commodity avg `0.0827` n `12`; crypto_alt avg `-0.3263` n `229`; crypto_major avg `-0.1112` n `8`; equity avg `0.1159` n `88`; fx avg `0.0082` n `6`; index avg `-0.0563` n `25`; metal avg `-0.0076` n `20`; unknown avg `-0.1853` n `765`
- 24h: commodity avg `0.1825` n `12`; crypto_alt avg `2.9894` n `229`; crypto_major avg `3.5558` n `8`; equity avg `1.9067` n `88`; fx avg `-0.1593` n `6`; index avg `0.4422` n `25`; metal avg `0.3075` n `20`; unknown avg `4.0549` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
