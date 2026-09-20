# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T05:37:26.423841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0107` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0335` n `12`; crypto_alt avg `0.0987` n `234`; crypto_major avg `-0.0269` n `8`; equity avg `-0.0021` n `140`; fx avg `-0.0001` n `6`; index avg `-0.0002` n `26`; metal avg `-0.003` n `20`; unknown avg `2.1331` n `943`
- 1h: commodity avg `-0.0539` n `12`; crypto_alt avg `-0.1712` n `234`; crypto_major avg `-0.155` n `8`; equity avg `-0.0298` n `140`; fx avg `-0.006` n `6`; index avg `-0.0101` n `26`; metal avg `0.0147` n `20`; unknown avg `18.2737` n `941`
- 4h: commodity avg `0.1159` n `12`; crypto_alt avg `-1.0469` n `234`; crypto_major avg `-1.0856` n `8`; equity avg `-0.4112` n `140`; fx avg `0.0008` n `6`; index avg `-0.0749` n `26`; metal avg `-0.0377` n `20`; unknown avg `1.9647` n `925`
- 24h: commodity avg `0.1754` n `12`; crypto_alt avg `-0.319` n `234`; crypto_major avg `-2.1183` n `8`; equity avg `-0.254` n `140`; fx avg `-0.0719` n `6`; index avg `-0.0555` n `26`; metal avg `-0.0133` n `20`; unknown avg `2.8968` n `816`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
