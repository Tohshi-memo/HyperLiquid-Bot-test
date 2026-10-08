# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T04:52:26.185316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.107` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0028` n `13`; crypto_alt avg `-0.0659` n `235`; crypto_major avg `-0.0219` n `8`; equity avg `0.0174` n `150`; fx avg `0.0134` n `6`; index avg `0.0096` n `26`; metal avg `0.0206` n `20`; unknown avg `-0.1223` n `1077`
- 1h: commodity avg `0.0064` n `13`; crypto_alt avg `-0.6016` n `235`; crypto_major avg `-0.5264` n `8`; equity avg `0.1328` n `150`; fx avg `0.0075` n `6`; index avg `0.0395` n `26`; metal avg `-0.0058` n `20`; unknown avg `0.0781` n `1069`
- 4h: commodity avg `0.1872` n `13`; crypto_alt avg `-1.1521` n `235`; crypto_major avg `-1.1255` n `8`; equity avg `-0.4279` n `150`; fx avg `0.0569` n `6`; index avg `-0.0185` n `26`; metal avg `0.278` n `20`; unknown avg `-0.1755` n `1069`
- 24h: commodity avg `0.429` n `13`; crypto_alt avg `-0.9079` n `235`; crypto_major avg `-2.0657` n `8`; equity avg `-1.3316` n `150`; fx avg `-0.1131` n `6`; index avg `-0.2188` n `26`; metal avg `-0.1761` n `20`; unknown avg `247.1913` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
