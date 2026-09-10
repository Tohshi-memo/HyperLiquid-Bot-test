# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T11:07:28.663347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0634` n `12`; crypto_alt avg `-0.0836` n `233`; crypto_major avg `-0.1282` n `8`; equity avg `-0.1508` n `134`; fx avg `0.0047` n `6`; index avg `-0.0425` n `26`; metal avg `-0.0437` n `20`; unknown avg `-0.0367` n `795`
- 1h: commodity avg `0.0086` n `12`; crypto_alt avg `-0.2081` n `233`; crypto_major avg `-0.2913` n `8`; equity avg `-0.2142` n `134`; fx avg `0.0121` n `6`; index avg `-0.0484` n `26`; metal avg `-0.3893` n `20`; unknown avg `0.7642` n `795`
- 4h: commodity avg `0.2161` n `12`; crypto_alt avg `-0.7404` n `233`; crypto_major avg `-0.4666` n `8`; equity avg `-0.5376` n `134`; fx avg `0.0624` n `6`; index avg `-0.1154` n `26`; metal avg `-0.5911` n `20`; unknown avg `-0.0476` n `789`
- 24h: commodity avg `0.0046` n `12`; crypto_alt avg `-3.9578` n `233`; crypto_major avg `-2.6775` n `8`; equity avg `-0.9474` n `134`; fx avg `0.1191` n `6`; index avg `-0.0649` n `26`; metal avg `-0.3662` n `20`; unknown avg `-0.6259` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
