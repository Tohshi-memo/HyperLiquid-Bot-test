# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T23:22:30.569564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2157` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0864` n `13`; crypto_alt avg `0.5448` n `239`; crypto_major avg `0.5331` n `8`; equity avg `0.2132` n `158`; fx avg `-0.0039` n `6`; index avg `0.0199` n `27`; metal avg `0.0224` n `20`; unknown avg `2.019` n `1262`
- 1h: commodity avg `-0.2432` n `13`; crypto_alt avg `1.2732` n `239`; crypto_major avg `1.3117` n `8`; equity avg `0.4771` n `158`; fx avg `0.0093` n `6`; index avg `0.0793` n `27`; metal avg `0.178` n `20`; unknown avg `2.9755` n `1236`
- 4h: commodity avg `-0.0239` n `13`; crypto_alt avg `-0.9419` n `239`; crypto_major avg `-1.2834` n `8`; equity avg `-0.694` n `158`; fx avg `-0.0213` n `6`; index avg `-0.0677` n `27`; metal avg `0.078` n `20`; unknown avg `2.5114` n `1172`
- 24h: commodity avg `-0.1577` n `13`; crypto_alt avg `-2.262` n `239`; crypto_major avg `-1.4086` n `8`; equity avg `-0.135` n `158`; fx avg `0.0296` n `6`; index avg `-0.0287` n `27`; metal avg `0.0729` n `20`; unknown avg `1.0` n `1002`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
