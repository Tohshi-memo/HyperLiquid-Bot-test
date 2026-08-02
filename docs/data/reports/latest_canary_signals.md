# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T22:07:30.088757+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2023` n `12`; crypto_alt avg `-0.0029` n `230`; crypto_major avg `0.0966` n `8`; equity avg `-0.0241` n `102`; fx avg `-0.0267` n `6`; index avg `-0.0342` n `25`; metal avg `-0.1334` n `20`; unknown avg `-0.0333` n `783`
- 1h: commodity avg `-0.4116` n `12`; crypto_alt avg `0.2222` n `230`; crypto_major avg `0.3608` n `8`; equity avg `0.1526` n `102`; fx avg `-0.0003` n `6`; index avg `0.0055` n `25`; metal avg `-0.0553` n `20`; unknown avg `1.4514` n `783`
- 4h: commodity avg `-0.3165` n `12`; crypto_alt avg `0.3662` n `230`; crypto_major avg `0.729` n `8`; equity avg `0.3509` n `102`; fx avg `0.1101` n `6`; index avg `0.0285` n `25`; metal avg `0.0047` n `20`; unknown avg `2.6252` n `782`
- 24h: commodity avg `-1.3893` n `12`; crypto_alt avg `1.38` n `230`; crypto_major avg `1.979` n `8`; equity avg `1.5022` n `102`; fx avg `-0.0457` n `6`; index avg `0.304` n `25`; metal avg `0.2571` n `20`; unknown avg `1.5746` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
