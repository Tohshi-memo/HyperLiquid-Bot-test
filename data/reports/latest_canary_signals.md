# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T11:52:30.840544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0215` n `13`; crypto_alt avg `0.2533` n `235`; crypto_major avg `0.3149` n `8`; equity avg `0.0323` n `150`; fx avg `-0.0092` n `6`; index avg `0.0027` n `26`; metal avg `-0.0218` n `20`; unknown avg `1.2681` n `1078`
- 1h: commodity avg `0.0054` n `13`; crypto_alt avg `0.8696` n `235`; crypto_major avg `0.8475` n `8`; equity avg `0.2249` n `150`; fx avg `-0.0164` n `6`; index avg `0.0243` n `26`; metal avg `0.0706` n `20`; unknown avg `2.0759` n `1076`
- 4h: commodity avg `-0.0002` n `13`; crypto_alt avg `-0.0719` n `235`; crypto_major avg `0.2338` n `8`; equity avg `0.1155` n `150`; fx avg `-0.0756` n `6`; index avg `-0.0114` n `26`; metal avg `-0.0334` n `20`; unknown avg `1.8105` n `1006`
- 24h: commodity avg `-0.4335` n `13`; crypto_alt avg `-0.8909` n `235`; crypto_major avg `-0.7814` n `8`; equity avg `-0.0749` n `150`; fx avg `0.0515` n `6`; index avg `0.0665` n `26`; metal avg `0.5354` n `20`; unknown avg `7.448` n `949`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
