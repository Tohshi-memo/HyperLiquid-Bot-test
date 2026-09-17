# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T04:07:38.036279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `12`; crypto_alt avg `-0.1098` n `234`; crypto_major avg `-0.0728` n `8`; equity avg `0.0839` n `137`; fx avg `-0.0059` n `6`; index avg `0.0183` n `27`; metal avg `0.0026` n `20`; unknown avg `-0.1633` n `919`
- 1h: commodity avg `-0.0196` n `12`; crypto_alt avg `0.0339` n `234`; crypto_major avg `-0.0729` n `8`; equity avg `0.1615` n `137`; fx avg `0.0141` n `6`; index avg `0.0359` n `27`; metal avg `0.092` n `20`; unknown avg `-0.5257` n `919`
- 4h: commodity avg `0.1397` n `12`; crypto_alt avg `0.4746` n `234`; crypto_major avg `0.4131` n `8`; equity avg `0.1582` n `137`; fx avg `0.0542` n `6`; index avg `-0.0007` n `27`; metal avg `0.241` n `20`; unknown avg `0.0463` n `911`
- 24h: commodity avg `-0.3871` n `12`; crypto_alt avg `1.8364` n `234`; crypto_major avg `1.0892` n `8`; equity avg `1.1407` n `137`; fx avg `0.0152` n `6`; index avg `0.1013` n `27`; metal avg `-0.2159` n `20`; unknown avg `0.6335` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
