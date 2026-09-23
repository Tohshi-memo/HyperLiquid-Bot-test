# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T09:37:26.603002+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2626` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0469` n `12`; crypto_alt avg `-0.1762` n `234`; crypto_major avg `-0.2154` n `8`; equity avg `0.0127` n `140`; fx avg `-0.0081` n `6`; index avg `0.0003` n `26`; metal avg `-0.0392` n `20`; unknown avg `-0.2272` n `945`
- 1h: commodity avg `-0.0268` n `12`; crypto_alt avg `-0.2598` n `234`; crypto_major avg `-0.6267` n `8`; equity avg `-0.0452` n `140`; fx avg `-0.0443` n `6`; index avg `-0.0008` n `26`; metal avg `-0.0349` n `20`; unknown avg `0.5369` n `943`
- 4h: commodity avg `0.1861` n `12`; crypto_alt avg `-0.4078` n `234`; crypto_major avg `-1.2734` n `8`; equity avg `-0.018` n `140`; fx avg `0.0771` n `6`; index avg `-0.0108` n `26`; metal avg `-0.2364` n `20`; unknown avg `0.2407` n `921`
- 24h: commodity avg `0.4733` n `12`; crypto_alt avg `3.3787` n `234`; crypto_major avg `0.6164` n `8`; equity avg `1.2041` n `140`; fx avg `0.0004` n `6`; index avg `0.123` n `26`; metal avg `-0.0189` n `20`; unknown avg `1.2167` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
