# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T08:07:25.181881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1177` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0102` n `13`; crypto_alt avg `-0.0481` n `238`; crypto_major avg `-0.0853` n `8`; equity avg `-0.2539` n `156`; fx avg `0.0112` n `6`; index avg `0.0112` n `27`; metal avg `0.0389` n `20`; unknown avg `-0.0286` n `1194`
- 1h: commodity avg `0.2336` n `13`; crypto_alt avg `-0.559` n `238`; crypto_major avg `-1.114` n `8`; equity avg `-0.5343` n `156`; fx avg `0.0103` n `6`; index avg `0.0037` n `27`; metal avg `-0.0875` n `20`; unknown avg `-0.3299` n `1194`
- 4h: commodity avg `0.1935` n `13`; crypto_alt avg `1.0236` n `238`; crypto_major avg `-0.2166` n `8`; equity avg `-0.5505` n `156`; fx avg `0.0187` n `6`; index avg `0.0731` n `27`; metal avg `-0.1814` n `20`; unknown avg `1.2024` n `1174`
- 24h: commodity avg `0.1524` n `13`; crypto_alt avg `-3.1017` n `238`; crypto_major avg `-0.6888` n `8`; equity avg `-3.011` n `155`; fx avg `0.1197` n `6`; index avg `-0.2564` n `27`; metal avg `-0.7885` n `20`; unknown avg `29.4567` n `938`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
