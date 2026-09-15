# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T16:52:33.008455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2605` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0408` n `12`; crypto_alt avg `0.2118` n `233`; crypto_major avg `0.0958` n `8`; equity avg `0.1116` n `137`; fx avg `0.0134` n `6`; index avg `0.0113` n `27`; metal avg `0.0282` n `20`; unknown avg `-0.0398` n `917`
- 1h: commodity avg `0.1566` n `12`; crypto_alt avg `0.237` n `233`; crypto_major avg `-0.08` n `8`; equity avg `0.0246` n `137`; fx avg `0.0135` n `6`; index avg `0.006` n `27`; metal avg `0.0543` n `20`; unknown avg `0.0177` n `901`
- 4h: commodity avg `0.4814` n `12`; crypto_alt avg `-0.8521` n `233`; crypto_major avg `-1.4208` n `8`; equity avg `-0.8128` n `137`; fx avg `0.054` n `6`; index avg `-0.1603` n `27`; metal avg `-0.0147` n `20`; unknown avg `1.3669` n `873`
- 24h: commodity avg `0.5956` n `12`; crypto_alt avg `-2.3669` n `233`; crypto_major avg `-2.7279` n `8`; equity avg `-1.2966` n `137`; fx avg `0.2474` n `6`; index avg `-0.1996` n `27`; metal avg `-0.086` n `20`; unknown avg `0.3694` n `831`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
