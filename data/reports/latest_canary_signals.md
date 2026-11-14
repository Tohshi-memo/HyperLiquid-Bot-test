# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T19:07:28.262467+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5761` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0037` n `13`; crypto_alt avg `0.234` n `239`; crypto_major avg `0.2902` n `8`; equity avg `0.0744` n `162`; fx avg `0.0104` n `6`; index avg `0.0109` n `27`; metal avg `0.0002` n `20`; unknown avg `11.3593` n `1256`
- 1h: commodity avg `-0.0357` n `13`; crypto_alt avg `-0.2092` n `239`; crypto_major avg `-0.2186` n `8`; equity avg `-0.0194` n `162`; fx avg `0.0028` n `6`; index avg `0.0037` n `27`; metal avg `-0.0327` n `20`; unknown avg `9.0348` n `1260`
- 4h: commodity avg `-0.0568` n `13`; crypto_alt avg `-1.9207` n `239`; crypto_major avg `-1.6269` n `8`; equity avg `-0.5361` n `162`; fx avg `0.0055` n `6`; index avg `-0.0508` n `27`; metal avg `-0.1393` n `20`; unknown avg `5.0728` n `1252`
- 24h: commodity avg `0.0025` n `13`; crypto_alt avg `-7.0321` n `239`; crypto_major avg `-6.6646` n `8`; equity avg `-1.9512` n `162`; fx avg `-0.0264` n `6`; index avg `-0.1551` n `27`; metal avg `-0.3081` n `20`; unknown avg `1.8278` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
