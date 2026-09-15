# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T20:37:27.875640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.854` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8236` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0456` n `12`; crypto_alt avg `0.0092` n `233`; crypto_major avg `-0.0205` n `8`; equity avg `-0.0004` n `137`; fx avg `-0.0082` n `6`; index avg `-0.0021` n `27`; metal avg `-0.0161` n `20`; unknown avg `1.5414` n `914`
- 1h: commodity avg `-0.0229` n `12`; crypto_alt avg `-0.4004` n `233`; crypto_major avg `-0.3069` n `8`; equity avg `0.0237` n `137`; fx avg `-0.0099` n `6`; index avg `0.052` n `27`; metal avg `-0.0373` n `20`; unknown avg `3.2936` n `894`
- 4h: commodity avg `0.0061` n `12`; crypto_alt avg `-1.6397` n `233`; crypto_major avg `-1.7951` n `8`; equity avg `-0.2967` n `137`; fx avg `0.0163` n `6`; index avg `0.0285` n `27`; metal avg `0.0589` n `20`; unknown avg `3.3692` n `893`
- 24h: commodity avg `0.4867` n `12`; crypto_alt avg `-5.0675` n `233`; crypto_major avg `-6.0075` n `8`; equity avg `-1.2433` n `137`; fx avg `0.2207` n `6`; index avg `-0.0561` n `27`; metal avg `0.1576` n `20`; unknown avg `0.8305` n `843`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
