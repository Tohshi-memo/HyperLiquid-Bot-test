# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T19:52:27.260264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6363` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5173` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0248` n `12`; crypto_alt avg `0.0313` n `233`; crypto_major avg `0.1442` n `8`; equity avg `-0.0703` n `137`; fx avg `-0.0125` n `6`; index avg `0.0148` n `27`; metal avg `-0.0173` n `20`; unknown avg `145.2828` n `918`
- 1h: commodity avg `0.0285` n `12`; crypto_alt avg `0.6015` n `233`; crypto_major avg `0.4423` n `8`; equity avg `0.1278` n `137`; fx avg `-0.0004` n `6`; index avg `0.0018` n `27`; metal avg `-0.0839` n `20`; unknown avg `9.6151` n `916`
- 4h: commodity avg `0.1692` n `12`; crypto_alt avg `-1.1881` n `233`; crypto_major avg `-1.5312` n `8`; equity avg `-0.4777` n `137`; fx avg `0.0138` n `6`; index avg `-0.0139` n `27`; metal avg `0.1051` n `20`; unknown avg `4.1872` n `901`
- 24h: commodity avg `0.5645` n `12`; crypto_alt avg `-3.9324` n `233`; crypto_major avg `-4.5735` n `8`; equity avg `-1.2808` n `137`; fx avg `0.2244` n `6`; index avg `-0.1054` n `27`; metal avg `0.2215` n `20`; unknown avg `4.9866` n `831`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
