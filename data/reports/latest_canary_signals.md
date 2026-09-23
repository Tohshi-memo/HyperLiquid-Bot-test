# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T10:22:33.238010+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4095` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `-0.3517` n `234`; crypto_major avg `-0.2036` n `8`; equity avg `-0.0001` n `140`; fx avg `0.0007` n `6`; index avg `0.0039` n `26`; metal avg `-0.0217` n `20`; unknown avg `0.7106` n `946`
- 1h: commodity avg `-0.0407` n `12`; crypto_alt avg `-0.5584` n `234`; crypto_major avg `-0.4911` n `8`; equity avg `-0.0449` n `140`; fx avg `-0.0033` n `6`; index avg `-0.0046` n `26`; metal avg `-0.0565` n `20`; unknown avg `0.3308` n `943`
- 4h: commodity avg `0.1155` n `12`; crypto_alt avg `-0.8889` n `234`; crypto_major avg `-1.4375` n `8`; equity avg `-0.1167` n `140`; fx avg `0.0479` n `6`; index avg `-0.028` n `26`; metal avg `-0.2051` n `20`; unknown avg `0.9901` n `937`
- 24h: commodity avg `0.6013` n `12`; crypto_alt avg `3.5156` n `234`; crypto_major avg `0.4869` n `8`; equity avg `0.8123` n `140`; fx avg `0.0133` n `6`; index avg `0.066` n `26`; metal avg `-0.1015` n `20`; unknown avg `1.3317` n `842`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
