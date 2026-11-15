# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T08:52:29.822689+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0309` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0001` n `13`; crypto_alt avg `0.2463` n `239`; crypto_major avg `0.242` n `8`; equity avg `-0.0005` n `162`; fx avg `-0.0027` n `6`; index avg `-0.0017` n `27`; metal avg `0.0251` n `20`; unknown avg `0.0616` n `1263`
- 1h: commodity avg `0.0184` n `13`; crypto_alt avg `0.2235` n `239`; crypto_major avg `1.0526` n `8`; equity avg `0.1167` n `162`; fx avg `-0.01` n `6`; index avg `-0.0214` n `27`; metal avg `0.0463` n `20`; unknown avg `0.1418` n `1245`
- 4h: commodity avg `-0.007` n `13`; crypto_alt avg `-1.0394` n `239`; crypto_major avg `-1.0535` n `8`; equity avg `-0.242` n `162`; fx avg `-0.0094` n `6`; index avg `-0.0226` n `27`; metal avg `0.0691` n `20`; unknown avg `0.0894` n `1225`
- 24h: commodity avg `0.036` n `13`; crypto_alt avg `-5.2456` n `239`; crypto_major avg `-4.2576` n `8`; equity avg `-1.0066` n `162`; fx avg `0.0178` n `6`; index avg `-0.1038` n `27`; metal avg `-0.3864` n `20`; unknown avg `46.5518` n `1060`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
