# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T19:22:28.137293+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.02` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0379` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.038` n `12`; crypto_alt avg `-0.1757` n `228`; crypto_major avg `-0.1719` n `8`; equity avg `0.1068` n `69`; fx avg `0.0072` n `6`; index avg `0.0135` n `23`; metal avg `-0.0762` n `18`; unknown avg `-0.2552` n `422`
- 1h: commodity avg `0.0005` n `12`; crypto_alt avg `-0.7847` n `228`; crypto_major avg `-0.6835` n `8`; equity avg `-0.0342` n `69`; fx avg `0.0341` n `6`; index avg `0.1109` n `23`; metal avg `-0.0315` n `18`; unknown avg `-0.0095` n `422`
- 4h: commodity avg `0.6854` n `12`; crypto_alt avg `-0.5359` n `228`; crypto_major avg `-0.9608` n `8`; equity avg `0.03` n `69`; fx avg `-0.0113` n `6`; index avg `0.0771` n `23`; metal avg `-0.5367` n `18`; unknown avg `0.1549` n `422`
- 24h: commodity avg `-0.102` n `12`; crypto_alt avg `-4.0629` n `228`; crypto_major avg `-4.5858` n `8`; equity avg `0.2628` n `69`; fx avg `0.081` n `6`; index avg `0.2673` n `23`; metal avg `0.204` n `18`; unknown avg `-0.3403` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
