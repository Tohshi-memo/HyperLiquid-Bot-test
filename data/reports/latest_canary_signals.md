# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T20:12:59.651663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5905` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5044` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0284` n `12`; crypto_alt avg `-0.1785` n `233`; crypto_major avg `-0.1985` n `8`; equity avg `0.1342` n `137`; fx avg `-0.0002` n `6`; index avg `0.0364` n `27`; metal avg `0.0026` n `20`; unknown avg `2.433` n `900`
- 1h: commodity avg `0.0911` n `12`; crypto_alt avg `-0.4118` n `233`; crypto_major avg `-0.4834` n `8`; equity avg `0.0228` n `137`; fx avg `-0.0023` n `6`; index avg `0.0256` n `27`; metal avg `-0.0672` n `20`; unknown avg `1.3406` n `900`
- 4h: commodity avg `0.1231` n `12`; crypto_alt avg `-1.1722` n `233`; crypto_major avg `-1.4543` n `8`; equity avg `-0.202` n `137`; fx avg `-0.017` n `6`; index avg `0.0501` n `27`; metal avg `0.1362` n `20`; unknown avg `1.6486` n `885`
- 24h: commodity avg `0.5774` n `12`; crypto_alt avg `-4.1662` n `233`; crypto_major avg `-4.9807` n `8`; equity avg `-0.9686` n `137`; fx avg `0.2123` n `6`; index avg `-0.031` n `27`; metal avg `0.2362` n `20`; unknown avg `1.2187` n `843`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
