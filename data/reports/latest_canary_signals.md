# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T12:52:31.358015+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0869` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0534` n `13`; crypto_alt avg `-0.3962` n `235`; crypto_major avg `-0.3345` n `8`; equity avg `-0.0186` n `150`; fx avg `-0.0148` n `6`; index avg `-0.0121` n `26`; metal avg `0.0372` n `20`; unknown avg `1.5842` n `1076`
- 1h: commodity avg `-0.0807` n `13`; crypto_alt avg `-0.125` n `235`; crypto_major avg `-0.1484` n `8`; equity avg `-0.031` n `150`; fx avg `-0.0487` n `6`; index avg `-0.0095` n `26`; metal avg `-0.2671` n `20`; unknown avg `0.339` n `1068`
- 4h: commodity avg `0.1964` n `13`; crypto_alt avg `-1.5657` n `235`; crypto_major avg `-1.2561` n `8`; equity avg `-0.8272` n `150`; fx avg `-0.0755` n `6`; index avg `-0.1692` n `26`; metal avg `-0.4118` n `20`; unknown avg `1.7054` n `1068`
- 24h: commodity avg `1.3835` n `13`; crypto_alt avg `-5.6042` n `235`; crypto_major avg `-3.9092` n `8`; equity avg `-1.7656` n `150`; fx avg `-0.2123` n `6`; index avg `-0.3921` n `26`; metal avg `-0.7649` n `20`; unknown avg `814.3958` n `980`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
