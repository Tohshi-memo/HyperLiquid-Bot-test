# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T13:22:33.265636+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0177` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.034` n `13`; crypto_alt avg `-0.3007` n `235`; crypto_major avg `-0.112` n `8`; equity avg `-0.1282` n `151`; fx avg `-0.0132` n `6`; index avg `-0.0102` n `26`; metal avg `-0.0254` n `20`; unknown avg `-0.1859` n `1134`
- 1h: commodity avg `0.1029` n `13`; crypto_alt avg `-0.686` n `235`; crypto_major avg `-0.5253` n `8`; equity avg `-0.1222` n `151`; fx avg `0.0118` n `6`; index avg `-0.0252` n `26`; metal avg `-0.0001` n `20`; unknown avg `-0.122` n `1132`
- 4h: commodity avg `0.2815` n `13`; crypto_alt avg `-1.4396` n `235`; crypto_major avg `-1.0726` n `8`; equity avg `-0.3111` n `151`; fx avg `0.0092` n `6`; index avg `-0.0549` n `26`; metal avg `-0.0257` n `20`; unknown avg `-0.0497` n `1083`
- 24h: commodity avg `0.1972` n `13`; crypto_alt avg `0.37` n `235`; crypto_major avg `0.1299` n `8`; equity avg `-1.4557` n `151`; fx avg `-0.1284` n `6`; index avg `-0.1622` n `26`; metal avg `-0.0223` n `20`; unknown avg `-0.1772` n `911`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2359`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2049`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
