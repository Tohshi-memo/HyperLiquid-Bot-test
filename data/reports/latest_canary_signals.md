# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-15T20:22:27.652328+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `13`; crypto_alt avg `0.1337` n `236`; crypto_major avg `0.0778` n `8`; equity avg `-0.038` n `151`; fx avg `-0.0001` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0052` n `20`; unknown avg `-0.1571` n `1090`
- 1h: commodity avg `-0.0316` n `13`; crypto_alt avg `-0.1328` n `236`; crypto_major avg `-0.0706` n `8`; equity avg `0.1732` n `151`; fx avg `-0.0036` n `6`; index avg `-0.0032` n `26`; metal avg `0.0773` n `20`; unknown avg `0.9578` n `1066`
- 4h: commodity avg `-0.19` n `13`; crypto_alt avg `0.7339` n `236`; crypto_major avg `0.5372` n `8`; equity avg `1.6865` n `151`; fx avg `0.0055` n `6`; index avg `0.186` n `26`; metal avg `0.1606` n `20`; unknown avg `0.5702` n `1066`
- 24h: commodity avg `-0.1963` n `13`; crypto_alt avg `0.7126` n `236`; crypto_major avg `0.5599` n `8`; equity avg `0.1992` n `151`; fx avg `0.1685` n `6`; index avg `-0.0556` n `26`; metal avg `0.5314` n `20`; unknown avg `29.997` n `940`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `-0.1012`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0955`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0849`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0777`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0715`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0708`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0507`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0482`, n `668`, weak_sample_signal
