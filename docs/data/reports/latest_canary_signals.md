# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T11:22:32.061543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0791` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `0.1916` n `234`; crypto_major avg `0.0377` n `8`; equity avg `0.0172` n `141`; fx avg `0.003` n `6`; index avg `0.0095` n `26`; metal avg `0.0909` n `20`; unknown avg `0.1644` n `945`
- 1h: commodity avg `0.0109` n `12`; crypto_alt avg `0.8418` n `234`; crypto_major avg `0.6473` n `8`; equity avg `0.2932` n `141`; fx avg `0.016` n `6`; index avg `0.0501` n `26`; metal avg `0.1345` n `20`; unknown avg `0.5799` n `943`
- 4h: commodity avg `0.2627` n `12`; crypto_alt avg `-0.9968` n `234`; crypto_major avg `-1.1463` n `8`; equity avg `-0.3824` n `141`; fx avg `0.0111` n `6`; index avg `-0.0672` n `26`; metal avg `-0.1594` n `20`; unknown avg `0.6084` n `937`
- 24h: commodity avg `0.6049` n `12`; crypto_alt avg `-3.8727` n `234`; crypto_major avg `-3.4126` n `8`; equity avg `-2.0073` n `141`; fx avg `0.0123` n `6`; index avg `-0.4067` n `26`; metal avg `-0.3513` n `20`; unknown avg `586.2069` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
