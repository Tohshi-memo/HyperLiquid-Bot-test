# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T21:22:25.006009+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `0.5085` n `231`; crypto_major avg `0.4793` n `8`; equity avg `0.1848` n `124`; fx avg `-0.0011` n `6`; index avg `0.0232` n `25`; metal avg `0.0123` n `20`; unknown avg `0.4346` n `795`
- 1h: commodity avg `0.037` n `12`; crypto_alt avg `1.3413` n `231`; crypto_major avg `1.2343` n `8`; equity avg `1.335` n `124`; fx avg `-0.0136` n `6`; index avg `0.18` n `25`; metal avg `0.0568` n `20`; unknown avg `0.8086` n `795`
- 4h: commodity avg `-0.1702` n `12`; crypto_alt avg `0.9474` n `231`; crypto_major avg `0.9741` n `8`; equity avg `1.4678` n `124`; fx avg `-0.02` n `6`; index avg `0.1869` n `25`; metal avg `0.0007` n `20`; unknown avg `0.4564` n `795`
- 24h: commodity avg `0.3127` n `12`; crypto_alt avg `1.2669` n `231`; crypto_major avg `1.0034` n `8`; equity avg `1.1833` n `124`; fx avg `-0.0547` n `6`; index avg `0.1648` n `25`; metal avg `-0.3267` n `20`; unknown avg `0.941` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
