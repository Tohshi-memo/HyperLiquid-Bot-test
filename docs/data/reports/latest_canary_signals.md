# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T00:54:46.457259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.0612` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.8963` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7476` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0205` n `12`; crypto_alt avg `-0.026` n `233`; crypto_major avg `-0.0505` n `8`; equity avg `0.0336` n `136`; fx avg `-0.0097` n `6`; index avg `-0.0039` n `27`; metal avg `0.053` n `20`; unknown avg `1.5547` n `908`
- 1h: commodity avg `0.0679` n `12`; crypto_alt avg `0.1577` n `233`; crypto_major avg `-0.0024` n `8`; equity avg `0.292` n `136`; fx avg `0.0153` n `6`; index avg `0.0669` n `27`; metal avg `-0.0054` n `20`; unknown avg `1.7214` n `900`
- 4h: commodity avg `0.1174` n `12`; crypto_alt avg `-1.2742` n `233`; crypto_major avg `-1.8144` n `8`; equity avg `0.2468` n `136`; fx avg `0.0175` n `6`; index avg `0.0819` n `27`; metal avg `-0.0668` n `20`; unknown avg `4.263` n `888`
- 24h: commodity avg `-0.0948` n `12`; crypto_alt avg `1.0478` n `233`; crypto_major avg `1.9551` n `8`; equity avg `0.2746` n `136`; fx avg `0.0512` n `6`; index avg `0.0201` n `27`; metal avg `-0.4776` n `20`; unknown avg `6.6684` n `676`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
