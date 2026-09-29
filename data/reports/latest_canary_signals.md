# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T15:22:29.405709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0039` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0202` n `12`; crypto_alt avg `-0.5126` n `234`; crypto_major avg `-0.3732` n `8`; equity avg `-0.2646` n `141`; fx avg `-0.0095` n `6`; index avg `-0.0615` n `26`; metal avg `-0.0797` n `20`; unknown avg `2.1394` n `959`
- 1h: commodity avg `0.0463` n `12`; crypto_alt avg `-0.806` n `234`; crypto_major avg `-1.0941` n `8`; equity avg `-0.4413` n `141`; fx avg `0.0199` n `6`; index avg `-0.0902` n `26`; metal avg `-0.1513` n `20`; unknown avg `3.3` n `899`
- 4h: commodity avg `-0.1487` n `12`; crypto_alt avg `-0.1` n `234`; crypto_major avg `-0.6446` n `8`; equity avg `0.1374` n `141`; fx avg `-0.0004` n `6`; index avg `-0.0766` n `26`; metal avg `-0.1725` n `20`; unknown avg `2.4597` n `893`
- 24h: commodity avg `-0.7952` n `12`; crypto_alt avg `2.7524` n `234`; crypto_major avg `0.7054` n `8`; equity avg `1.3465` n `141`; fx avg `-0.1493` n `6`; index avg `0.0922` n `26`; metal avg `-0.0608` n `20`; unknown avg `14.7273` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1848`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1725`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
