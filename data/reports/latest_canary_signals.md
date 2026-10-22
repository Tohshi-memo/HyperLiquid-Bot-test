# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T04:52:33.376615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.72` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.5399` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0378` n `13`; crypto_alt avg `-0.0313` n `237`; crypto_major avg `0.0638` n `8`; equity avg `0.0687` n `151`; fx avg `-0.0029` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.6845` n `1201`
- 1h: commodity avg `0.0291` n `13`; crypto_alt avg `-0.1852` n `237`; crypto_major avg `0.0096` n `8`; equity avg `-0.1001` n `151`; fx avg `-0.0105` n `6`; index avg `-0.0483` n `26`; metal avg `-0.0041` n `20`; unknown avg `0.2158` n `1189`
- 4h: commodity avg `0.1846` n `13`; crypto_alt avg `-2.1864` n `237`; crypto_major avg `-1.7814` n `8`; equity avg `-1.4957` n `151`; fx avg `-0.0605` n `6`; index avg `-0.2415` n `26`; metal avg `-0.4986` n `20`; unknown avg `5.9098` n `1177`
- 24h: commodity avg `-0.4692` n `13`; crypto_alt avg `-0.5824` n `237`; crypto_major avg `-0.4051` n `8`; equity avg `-2.0259` n `151`; fx avg `-0.0135` n `6`; index avg `-0.3036` n `26`; metal avg `-0.5013` n `20`; unknown avg `118.6434` n `930`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
