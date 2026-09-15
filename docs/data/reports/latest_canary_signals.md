# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T19:37:32.122896+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7418` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5317` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1198` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0308` n `12`; crypto_alt avg `-0.3204` n `233`; crypto_major avg `-0.3827` n `8`; equity avg `-0.0784` n `137`; fx avg `0.0173` n `6`; index avg `-0.0185` n `27`; metal avg `-0.0145` n `20`; unknown avg `14.0694` n `918`
- 1h: commodity avg `-0.0363` n `12`; crypto_alt avg `-0.5741` n `233`; crypto_major avg `-1.1514` n `8`; equity avg `-0.0332` n `137`; fx avg `0.0114` n `6`; index avg `-0.0316` n `27`; metal avg `-0.0055` n `20`; unknown avg `0.3749` n `916`
- 4h: commodity avg `0.091` n `12`; crypto_alt avg `-1.2515` n `233`; crypto_major avg `-1.5629` n `8`; equity avg `-0.3572` n `137`; fx avg `-0.0009` n `6`; index avg `-0.0312` n `27`; metal avg `0.1789` n `20`; unknown avg `0.7124` n `901`
- 24h: commodity avg `0.5705` n `12`; crypto_alt avg `-3.8715` n `233`; crypto_major avg `-4.6672` n `8`; equity avg `-1.3197` n `137`; fx avg `0.2372` n `6`; index avg `-0.1391` n `27`; metal avg `0.1711` n `20`; unknown avg `0.3141` n `831`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
