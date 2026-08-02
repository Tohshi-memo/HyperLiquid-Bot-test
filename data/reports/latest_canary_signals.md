# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T00:37:27.934139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0324` n `12`; crypto_alt avg `-0.1486` n `230`; crypto_major avg `-0.1172` n `8`; equity avg `0.0141` n `102`; fx avg `0.0086` n `6`; index avg `0.0155` n `25`; metal avg `0.0058` n `20`; unknown avg `-0.1392` n `782`
- 1h: commodity avg `-0.1695` n `12`; crypto_alt avg `0.1383` n `230`; crypto_major avg `0.0448` n `8`; equity avg `0.3016` n `102`; fx avg `0.0395` n `6`; index avg `0.0622` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.2515` n `782`
- 4h: commodity avg `-0.3045` n `12`; crypto_alt avg `0.4201` n `230`; crypto_major avg `0.4317` n `8`; equity avg `0.6016` n `102`; fx avg `0.0109` n `6`; index avg `0.0859` n `25`; metal avg `0.0509` n `20`; unknown avg `-0.1432` n `782`
- 24h: commodity avg `-0.2119` n `12`; crypto_alt avg `-0.7285` n `230`; crypto_major avg `-0.7893` n `8`; equity avg `0.1985` n `102`; fx avg `-0.05` n `6`; index avg `0.0609` n `25`; metal avg `0.0606` n `20`; unknown avg `-0.0452` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
