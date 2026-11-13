# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T17:37:29.598418+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3008` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0179` n `13`; crypto_alt avg `0.5751` n `239`; crypto_major avg `0.5912` n `8`; equity avg `0.3421` n `162`; fx avg `-0.006` n `6`; index avg `0.0357` n `27`; metal avg `0.0316` n `20`; unknown avg `0.3452` n `1262`
- 1h: commodity avg `-0.0565` n `13`; crypto_alt avg `-0.0628` n `239`; crypto_major avg `0.395` n `8`; equity avg `0.5976` n `162`; fx avg `-0.0166` n `6`; index avg `0.0568` n `27`; metal avg `-0.0021` n `20`; unknown avg `1.7242` n `1260`
- 4h: commodity avg `-0.2702` n `13`; crypto_alt avg `-1.2355` n `239`; crypto_major avg `-1.5832` n `8`; equity avg `-2.9199` n `162`; fx avg `-0.0922` n `6`; index avg `-0.2824` n `27`; metal avg `-0.3194` n `20`; unknown avg `1.2447` n `1248`
- 24h: commodity avg `0.0145` n `13`; crypto_alt avg `0.4053` n `239`; crypto_major avg `-1.3924` n `8`; equity avg `-3.1487` n `162`; fx avg `-0.0362` n `6`; index avg `-0.2817` n `27`; metal avg `-0.184` n `20`; unknown avg `1.5757` n `1089`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
