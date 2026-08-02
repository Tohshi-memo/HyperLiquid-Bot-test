# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T04:44:34.633171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3232` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0237` n `12`; crypto_alt avg `0.0431` n `230`; crypto_major avg `-0.0471` n `8`; equity avg `0.0099` n `102`; fx avg `0.0187` n `6`; index avg `-0.0307` n `25`; metal avg `-0.0226` n `20`; unknown avg `0.2155` n `782`
- 1h: commodity avg `0.036` n `12`; crypto_alt avg `0.091` n `230`; crypto_major avg `0.0544` n `8`; equity avg `0.067` n `102`; fx avg `-0.0115` n `6`; index avg `-0.0148` n `25`; metal avg `0.02` n `20`; unknown avg `0.0004` n `782`
- 4h: commodity avg `-1.0216` n `12`; crypto_alt avg `1.055` n `230`; crypto_major avg `1.3016` n `8`; equity avg `0.7322` n `102`; fx avg `-0.0331` n `6`; index avg `0.1737` n `25`; metal avg `0.1823` n `20`; unknown avg `5.8992` n `782`
- 24h: commodity avg `-1.1889` n `12`; crypto_alt avg `0.0356` n `230`; crypto_major avg `0.3416` n `8`; equity avg `0.8704` n `102`; fx avg `-0.0979` n `6`; index avg `0.1918` n `25`; metal avg `0.2611` n `20`; unknown avg `0.0287` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
