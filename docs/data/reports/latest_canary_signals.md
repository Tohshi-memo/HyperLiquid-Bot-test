# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T00:07:27.303499+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5688` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.3927` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `0.085` n `233`; crypto_major avg `0.0175` n `8`; equity avg `0.0263` n `136`; fx avg `-0.0089` n `6`; index avg `0.013` n `27`; metal avg `-0.0106` n `20`; unknown avg `0.5525` n `906`
- 1h: commodity avg `0.021` n `12`; crypto_alt avg `-0.0623` n `233`; crypto_major avg `-0.2582` n `8`; equity avg `-0.0108` n `136`; fx avg `0.0173` n `6`; index avg `0.0322` n `27`; metal avg `-0.0723` n `20`; unknown avg `0.4088` n `906`
- 4h: commodity avg `0.0623` n `12`; crypto_alt avg `-0.8116` n `233`; crypto_major avg `-1.329` n `8`; equity avg `0.2398` n `136`; fx avg `-0.0121` n `6`; index avg `0.0637` n `27`; metal avg `-0.0067` n `20`; unknown avg `0.5956` n `878`
- 24h: commodity avg `-0.0729` n `12`; crypto_alt avg `0.9626` n `233`; crypto_major avg `1.997` n `8`; equity avg `-0.2714` n `136`; fx avg `0.0003` n `6`; index avg `-0.0056` n `27`; metal avg `-0.4695` n `20`; unknown avg `6.2808` n `676`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
