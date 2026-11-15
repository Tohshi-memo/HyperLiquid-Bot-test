# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T16:52:28.498144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4268` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0091` n `13`; crypto_alt avg `-0.2893` n `239`; crypto_major avg `-0.1241` n `8`; equity avg `-0.0116` n `162`; fx avg `0.007` n `6`; index avg `-0.0027` n `27`; metal avg `-0.0162` n `20`; unknown avg `1.8387` n `1265`
- 1h: commodity avg `-0.001` n `13`; crypto_alt avg `-0.0799` n `239`; crypto_major avg `-0.1041` n `8`; equity avg `0.2976` n `162`; fx avg `0.0099` n `6`; index avg `0.0235` n `27`; metal avg `0.0109` n `20`; unknown avg `2.573` n `1256`
- 4h: commodity avg `-0.0663` n `13`; crypto_alt avg `-1.5964` n `239`; crypto_major avg `-1.3887` n `8`; equity avg `0.0734` n `162`; fx avg `-0.0015` n `6`; index avg `0.0381` n `27`; metal avg `-0.0357` n `20`; unknown avg `160.1204` n `1255`
- 24h: commodity avg `0.0687` n `13`; crypto_alt avg `-1.2339` n `239`; crypto_major avg `-0.6798` n `8`; equity avg `0.4307` n `162`; fx avg `-0.0161` n `6`; index avg `0.0833` n `27`; metal avg `-0.1473` n `20`; unknown avg `0.5571` n `1136`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
