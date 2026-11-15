# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T15:52:26.194773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1636` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0072` n `13`; crypto_alt avg `-0.1498` n `239`; crypto_major avg `-0.0835` n `8`; equity avg `0.0005` n `162`; fx avg `-0.0027` n `6`; index avg `0.0011` n `27`; metal avg `-0.0045` n `20`; unknown avg `-0.1259` n `1264`
- 1h: commodity avg `0.045` n `13`; crypto_alt avg `-0.1956` n `239`; crypto_major avg `-0.2549` n `8`; equity avg `0.0421` n `162`; fx avg `-0.0039` n `6`; index avg `0.0116` n `27`; metal avg `-0.0063` n `20`; unknown avg `-0.0049` n `1262`
- 4h: commodity avg `-0.053` n `13`; crypto_alt avg `-1.0909` n `239`; crypto_major avg `-1.1563` n `8`; equity avg `-0.209` n `162`; fx avg `-0.0177` n `6`; index avg `0.0073` n `27`; metal avg `-0.0246` n `20`; unknown avg `0.2902` n `1253`
- 24h: commodity avg `0.0339` n `13`; crypto_alt avg `-2.5967` n `239`; crypto_major avg `-1.6323` n `8`; equity avg `-0.2767` n `162`; fx avg `-0.0197` n `6`; index avg `0.0066` n `27`; metal avg `-0.1236` n `20`; unknown avg `0.1754` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
