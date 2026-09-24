# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T22:37:37.389040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0402` n `12`; crypto_alt avg `0.2326` n `234`; crypto_major avg `0.1568` n `8`; equity avg `0.0066` n `141`; fx avg `-0.0021` n `6`; index avg `0.0027` n `26`; metal avg `0.0173` n `20`; unknown avg `0.0621` n `946`
- 1h: commodity avg `-0.1758` n `12`; crypto_alt avg `-0.563` n `234`; crypto_major avg `-0.5132` n `8`; equity avg `-0.0242` n `141`; fx avg `-0.009` n `6`; index avg `0.0018` n `26`; metal avg `0.0136` n `20`; unknown avg `1.3368` n `904`
- 4h: commodity avg `-0.2751` n `12`; crypto_alt avg `0.28` n `234`; crypto_major avg `-0.41` n `8`; equity avg `0.0103` n `141`; fx avg `-0.0355` n `6`; index avg `-0.0074` n `26`; metal avg `-0.0199` n `20`; unknown avg `6.1879` n `829`
- 24h: commodity avg `0.5982` n `12`; crypto_alt avg `3.8781` n `234`; crypto_major avg `0.8144` n `8`; equity avg `-0.3417` n `141`; fx avg `0.0186` n `6`; index avg `-0.1204` n `26`; metal avg `-0.1423` n `20`; unknown avg `21.2291` n `815`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
