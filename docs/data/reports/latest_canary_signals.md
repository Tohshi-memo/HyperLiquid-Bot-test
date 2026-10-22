# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T02:22:28.215319+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2918` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `2.03` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.8389` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7656` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.2859` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0393` n `13`; crypto_alt avg `-0.4942` n `237`; crypto_major avg `-0.3524` n `8`; equity avg `-0.2376` n `151`; fx avg `0.0023` n `6`; index avg `-0.0366` n `26`; metal avg `0.0245` n `20`; unknown avg `9.5249` n `1201`
- 1h: commodity avg `0.0157` n `13`; crypto_alt avg `-1.7661` n `237`; crypto_major avg `-1.3809` n `8`; equity avg `-0.8676` n `151`; fx avg `-0.0409` n `6`; index avg `-0.095` n `26`; metal avg `-0.1188` n `20`; unknown avg `12.1646` n `1199`
- 4h: commodity avg `0.1721` n `13`; crypto_alt avg `-2.3965` n `237`; crypto_major avg `-2.1197` n `8`; equity avg `-2.0522` n `151`; fx avg `-0.0657` n `6`; index avg `-0.2808` n `26`; metal avg `-0.3541` n `20`; unknown avg `10.6747` n `1042`
- 24h: commodity avg `-0.6174` n `13`; crypto_alt avg `-0.2521` n `237`; crypto_major avg `-0.4303` n `8`; equity avg `-1.8492` n `151`; fx avg `-0.0576` n `6`; index avg `-0.2678` n `26`; metal avg `-0.4109` n `20`; unknown avg `122.1541` n `945`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1665`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
