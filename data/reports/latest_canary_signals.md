# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T02:07:31.721207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0319` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0387` n `12`; crypto_alt avg `-0.3809` n `234`; crypto_major avg `-0.4703` n `8`; equity avg `-0.0878` n `141`; fx avg `-0.0091` n `6`; index avg `-0.0134` n `26`; metal avg `-0.114` n `20`; unknown avg `-0.2732` n `943`
- 1h: commodity avg `0.1372` n `12`; crypto_alt avg `-0.5195` n `234`; crypto_major avg `-0.8968` n `8`; equity avg `-0.1705` n `141`; fx avg `-0.0072` n `6`; index avg `-0.036` n `26`; metal avg `-0.1713` n `20`; unknown avg `0.4216` n `943`
- 4h: commodity avg `-0.0397` n `12`; crypto_alt avg `-0.7967` n `234`; crypto_major avg `-1.1222` n `8`; equity avg `-0.3595` n `141`; fx avg `0.0099` n `6`; index avg `-0.0903` n `26`; metal avg `-0.1871` n `20`; unknown avg `0.1312` n `937`
- 24h: commodity avg `0.5223` n `12`; crypto_alt avg `-4.3237` n `234`; crypto_major avg `-3.9457` n `8`; equity avg `-1.5379` n `140`; fx avg `0.0577` n `6`; index avg `-0.3166` n `26`; metal avg `-0.7287` n `20`; unknown avg `583.1811` n `821`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
