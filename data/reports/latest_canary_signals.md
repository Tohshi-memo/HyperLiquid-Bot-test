# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T13:22:28.030434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1898` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.3882` n `13`; crypto_alt avg `-0.4563` n `239`; crypto_major avg `-0.4342` n `8`; equity avg `-0.5248` n `162`; fx avg `0.018` n `6`; index avg `-0.0453` n `27`; metal avg `-0.1516` n `20`; unknown avg `0.0155` n `1259`
- 1h: commodity avg `0.384` n `13`; crypto_alt avg `-0.5395` n `239`; crypto_major avg `-0.5886` n `8`; equity avg `-0.8848` n `162`; fx avg `0.0137` n `6`; index avg `-0.0777` n `27`; metal avg `-0.1506` n `20`; unknown avg `2.7596` n `1251`
- 4h: commodity avg `0.1685` n `13`; crypto_alt avg `-1.0795` n `239`; crypto_major avg `-1.2648` n `8`; equity avg `-1.2511` n `162`; fx avg `-0.0103` n `6`; index avg `-0.075` n `27`; metal avg `-0.1622` n `20`; unknown avg `21.3231` n `1247`
- 24h: commodity avg `0.1547` n `13`; crypto_alt avg `-3.2389` n `239`; crypto_major avg `-2.5556` n `8`; equity avg `-2.5921` n `162`; fx avg `-0.0666` n `6`; index avg `-0.1775` n `27`; metal avg `-1.0186` n `20`; unknown avg `0.9548` n `1138`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
