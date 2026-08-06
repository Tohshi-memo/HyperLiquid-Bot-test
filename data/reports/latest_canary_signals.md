# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T10:37:33.170017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0144` n `12`; crypto_alt avg `-0.0256` n `230`; crypto_major avg `-0.015` n `8`; equity avg `-0.0945` n `108`; fx avg `-0.0045` n `6`; index avg `-0.0148` n `25`; metal avg `0.004` n `20`; unknown avg `0.1002` n `782`
- 1h: commodity avg `0.096` n `12`; crypto_alt avg `-0.0846` n `230`; crypto_major avg `-0.1753` n `8`; equity avg `0.0792` n `108`; fx avg `-0.0206` n `6`; index avg `0.0086` n `25`; metal avg `-0.0439` n `20`; unknown avg `108.1583` n `782`
- 4h: commodity avg `-0.0187` n `12`; crypto_alt avg `-0.3599` n `230`; crypto_major avg `-0.5386` n `8`; equity avg `-0.0967` n `108`; fx avg `-0.0091` n `6`; index avg `-0.0056` n `25`; metal avg `0.1935` n `20`; unknown avg `108.1174` n `782`
- 24h: commodity avg `-0.1655` n `12`; crypto_alt avg `-0.0642` n `230`; crypto_major avg `-0.5699` n `8`; equity avg `-1.5761` n `108`; fx avg `-0.0242` n `6`; index avg `-0.3161` n `25`; metal avg `0.5761` n `20`; unknown avg `112.8796` n `750`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
