# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T10:37:26.209169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2144` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0249` n `13`; crypto_alt avg `-0.4348` n `235`; crypto_major avg `-0.3507` n `8`; equity avg `-0.1258` n `151`; fx avg `0.0132` n `6`; index avg `-0.0368` n `26`; metal avg `-0.0014` n `20`; unknown avg `-0.0395` n `1135`
- 1h: commodity avg `-0.0641` n `13`; crypto_alt avg `-0.7484` n `235`; crypto_major avg `-0.4771` n `8`; equity avg `-0.2894` n `151`; fx avg `0.0078` n `6`; index avg `-0.046` n `26`; metal avg `-0.0126` n `20`; unknown avg `0.4521` n `1133`
- 4h: commodity avg `-0.1997` n `13`; crypto_alt avg `-1.8033` n `235`; crypto_major avg `-1.1575` n `8`; equity avg `0.1463` n `151`; fx avg `-0.0265` n `6`; index avg `0.0569` n `26`; metal avg `0.0607` n `20`; unknown avg `0.2547` n `1117`
- 24h: commodity avg `-0.0441` n `13`; crypto_alt avg `-4.4853` n `235`; crypto_major avg `-2.7213` n `8`; equity avg `-2.901` n `151`; fx avg `0.0503` n `6`; index avg `-0.3557` n `26`; metal avg `-0.0391` n `20`; unknown avg `0.1326` n `973`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1811`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1661`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1642`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1446`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0739`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
