# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T21:37:37.952330+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.3676` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `-0.2776` n `233`; crypto_major avg `-0.3442` n `8`; equity avg `-0.0311` n `136`; fx avg `-0.0011` n `6`; index avg `-0.0023` n `27`; metal avg `-0.0095` n `20`; unknown avg `2.3539` n `908`
- 1h: commodity avg `0.0214` n `12`; crypto_alt avg `-1.0736` n `233`; crypto_major avg `-1.3614` n `8`; equity avg `-0.0448` n `136`; fx avg `0.004` n `6`; index avg `0.0062` n `27`; metal avg `0.0376` n `20`; unknown avg `8.8141` n `896`
- 4h: commodity avg `0.0268` n `12`; crypto_alt avg `-0.0958` n `233`; crypto_major avg `0.2975` n `8`; equity avg `-0.478` n `136`; fx avg `0.0027` n `6`; index avg `-0.0871` n `27`; metal avg `-0.0802` n `20`; unknown avg `9.4975` n `874`
- 24h: commodity avg `0.1911` n `12`; crypto_alt avg `-0.0967` n `233`; crypto_major avg `1.8217` n `8`; equity avg `-0.729` n `136`; fx avg `0.0342` n `6`; index avg `-0.2261` n `27`; metal avg `-0.3974` n `20`; unknown avg `6.3087` n `684`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
