# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T16:22:32.108538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3988` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0142` n `13`; crypto_alt avg `0.013` n `239`; crypto_major avg `-0.2089` n `8`; equity avg `0.0377` n `162`; fx avg `0.0019` n `6`; index avg `0.0048` n `27`; metal avg `0.0014` n `20`; unknown avg `21.7453` n `1263`
- 1h: commodity avg `-0.0211` n `13`; crypto_alt avg `0.0007` n `239`; crypto_major avg `-0.1877` n `8`; equity avg `0.1636` n `162`; fx avg `0.0045` n `6`; index avg `0.0309` n `27`; metal avg `0.0258` n `20`; unknown avg `-0.1865` n `1256`
- 4h: commodity avg `-0.0727` n `13`; crypto_alt avg `-1.1932` n `239`; crypto_major avg `-1.3718` n `8`; equity avg `-0.0928` n `162`; fx avg `-0.0107` n `6`; index avg `0.027` n `27`; metal avg `-0.0328` n `20`; unknown avg `159.7691` n `1255`
- 24h: commodity avg `0.0149` n `13`; crypto_alt avg `-1.2414` n `239`; crypto_major avg `-1.0094` n `8`; equity avg `0.0718` n `162`; fx avg `-0.007` n `6`; index avg `0.0507` n `27`; metal avg `-0.1008` n `20`; unknown avg `0.4747` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
